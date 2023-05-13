from src.gui.console_handler import ConsoleHandler
from src.heap.heap import Heap

ch = ConsoleHandler('./configuration/data.json')
ch.load_json_configuration('./configuration/data.json')
heap = Heap(ch.heap.heap)

heap.print_heap()
heap.heap_extract_max()
heap.heap_extract_min()

heap.print_heap()
print("adding 9")
heap.heap_insert(9)

heap.print_heap()
print("adding 1")
heap.heap_insert(1)

heap.print_heap()
ch.load_json_configuration('./configuration/data2.json')
heap2 = Heap(ch.heap.heap)
ConsoleHandler('./configuration/data2.json')
print("adding 9")
heap2.heap_insert(9)
heap.print_heap()
print("removing 2")
heap2.heap_delete(2)
heap2.print_heap()
