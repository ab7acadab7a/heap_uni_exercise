from src.gui.console_handler import ConsoleHandler

ch = ConsoleHandler('./configuration/data.json')

ch.heap.heapify(0)
ch.heap.print_heap()
