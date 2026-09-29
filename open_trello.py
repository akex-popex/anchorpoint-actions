import anchorpoint as ap
import webbrowser


def main():
    ctx = ap.get_context()
    ui = ap.UI()

    url = ctx.inputs.get("url")

    if not url or "your_board_id" in url:
        ui.show_error(
            "Trello URL Not Set",
            "Edit the 'url' input in open_trello.yaml and set it to your board's link."
        )
        return

    webbrowser.open(url)


if __name__ == "__main__":
    main()