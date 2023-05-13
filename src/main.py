from src.console_handler import ConsoleHandler

# fill if there are errors with the dir (default should be automatic for your correct path)
root_path = ""


if __name__ == '__main__':
    ch = ConsoleHandler(root_path)
    ch.run()

