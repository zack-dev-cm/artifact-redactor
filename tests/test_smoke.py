from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = REPO_ROOT / "skill" / "artifact-redactor" / "scripts"


class ArtifactRedactorSmokeTest(unittest.TestCase):
    def test_end_to_end_redaction_flow(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            source = tmp_path / "raw"
            source.mkdir()
            github_token = "ghp_" + "123456789012345678901234567890123456"
            localhost_url = "http://" + "local" + "host:3000/upload?token=abc"
            credential_url = "https://" + "user:pass@" + "example.com/private?x=1"
            unix_path = "/Users" + "/zack/private/demo.json"
            file_url = "file://" + "tmp/output.log"
            bearer_token = "Bearer " + "demo-demo-demo-demo"
            windows_path = "C:" + "\\Users\\zack\\Desktop\\secret.txt"

            (source / "notes.md").write_text(
                "\n".join(
                    [
                        f"Token {github_token} is in this draft.",
                        f"Private endpoint {localhost_url} should not be shared.",
                        f"Credentialed URL {credential_url} should be treated as private.",
                        f"Path {unix_path} and {file_url} are local only.",
                        "Email person@example.com and phone +1 (555) 123-4567 are present.",
                        "Public docs https://example.com/docs?page=2#proof can stay without the query string.",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )
            (source / "report.json").write_text(
                json.dumps({"note": f"{bearer_token} should be removed", "path": windows_path}) + "\n",
                encoding="utf-8",
            )
            (source / "capture.png").write_bytes(b"\x89PNG\r\n\x1a\nbinary")

            scan_path = tmp_path / "scan.json"
            redaction_path = tmp_path / "redaction.json"
            check_path = tmp_path / "check.json"
            report_path = tmp_path / "report.md"
            safe_dir = tmp_path / "safe"

            self.run_script("scan_sensitive_text.py", "--root", str(source), "--out", str(scan_path))
            self.run_script(
                "redact_artifacts.py",
                "--root",
                str(source),
                "--out-dir",
                str(safe_dir),
                "--out",
                str(redaction_path),
            )
            self.run_script("check_redaction_output.py", "--root", str(safe_dir), "--out", str(check_path))
            self.run_script(
                "render_redaction_report.py",
                "--scan",
                str(scan_path),
                "--redaction",
                str(redaction_path),
                "--check",
                str(check_path),
                "--out",
                str(report_path),
            )

            scan = json.loads(scan_path.read_text(encoding="utf-8"))
            redaction = json.loads(redaction_path.read_text(encoding="utf-8"))
            check = json.loads(check_path.read_text(encoding="utf-8"))
            report = report_path.read_text(encoding="utf-8")
            notes = (safe_dir / "notes.md").read_text(encoding="utf-8")
            report_json = (safe_dir / "report.json").read_text(encoding="utf-8")

            self.assertGreater(scan["finding_count"], 0)
            self.assertEqual(check["status"], "share-ready")
            self.assertEqual(check["finding_count"], 0)
            self.assertIn("[redacted-secret]", notes)
            self.assertIn("[redacted-private-url]", notes)
            self.assertIn("[redacted-private-path]", notes)
            self.assertIn("[redacted-email]", notes)
            self.assertIn("[redacted-phone]", notes)
            self.assertIn("https://example.com/docs", notes)
            self.assertNotIn("?page=2", notes)
            self.assertIn("[redacted-secret]", report_json)
            self.assertFalse((safe_dir / "capture.png").exists())
            self.assertEqual(len(redaction["skipped_files"]), 1)
            self.assertIn("Recommendation: **Share**", report)
            self.assertIn("capture.png", report)

    def run_script(self, script_name: str, *args: str) -> None:
        script_path = SCRIPTS / script_name
        subprocess.run([sys.executable, str(script_path), *args], check=True, cwd=REPO_ROOT)


if __name__ == "__main__":
    unittest.main()
