from src.gui.console_handler import ConsoleHandler

ch = ConsoleHandler('./configuration/data.json')

ch.heap.print_heap()
ch.heap.heap_extract_max()
ch.heap.heap_extract_min()

ch.heap.print_heap()
print("adding 9")
ch.heap.heap_insert(9)

ch.heap.print_heap()
print("adding 1")
ch.heap.heap_insert(1)

ch.heap.print_heap()

ch = ConsoleHandler('./configuration/data2.json')
print("adding 9")
ch.heap.heap_insert(9)
ch.heap.print_heap()
print("removing 2")
ch.heap.heap_delete(2)
ch.heap.print_heap()
