import anchorpoint as ap
import subprocess
import shutil
import os


def main():
    ctx = ap.get_context()
    ui = ap.UI()

    project_root = ctx.project_path
    if not project_root:
        ui.show_error("No Project", "This action has to be run inside an Anchorpoint project.")
        return

    # Unity project lives in the "engine" subfolder of the repo
    unity_project_path = os.path.join(project_root, "engine")

    if not os.path.isdir(unity_project_path):
        ui.show_error("Unity Project Not Found", f"Could not find a Unity project at {unity_project_path}")
        return

    unity_cli = shutil.which("unity")
    if not unity_cli:
        ui.show_error(
            "Unity CLI Not Found",
            "Install it once with 'winget install Unity.CLI' (Windows) or "
            "'brew install --cask unity-cli' (macOS), then try again."
        )
        return

    try:
        subprocess.Popen([unity_cli, "open", unity_project_path])
        ui.show_success("Opening Unity", f"Launching project at {unity_project_path}")
    except Exception as e:
        ap.log_error(f"Failed to open Unity project: {e}")
        ui.show_error("Failed to Open Unity", str(e))


if __name__ == "__main__":
    main()