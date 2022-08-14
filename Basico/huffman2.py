from heapq import heappush, heappop, heapify
from collections import defaultdict
from bitarray import bitarray

text = "Texto de Prueba"

freq_lib = defaultdict(int)    
for ch in text:                
    freq_lib[ch] += 1
    
print(freq_lib)

heap = [[fq, [sym, ""]] for sym, fq in freq_lib.items()]  
print(heap)


heapify(heap) # transform the list into a heap tree structure
print(heap)

while len(heap) > 1:
    right = heappop(heap)  
    print('right = ', right)
    left = heappop(heap)
    print('left = ', left)

    for pair in right[1:]:  
        pair[1] = '0' + pair[1]   
    for pair in left[1:]:  
        pair[1] = '1' + pair[1]   
    heappush(heap, [right[0] + left[0]] + right[1:] + left[1:])  

huffman_list = right[1:] + left[1:]
print(huffman_list)
huffman_dict = {a[0]:bitarray(str(a[1])) for a in huffman_list}
print(huffman_dict)

# **************** Huffman Encoding **********************

encoded_text = bitarray()
encoded_text.encode(huffman_dict, text)
print(encoded_text)

padding = 8 - (len(encoded_text) % 8)

with open('compressed_file.bin', 'wb') as w:
    encoded_text.tofile(w)


# **************** Huffman Decoding **********************

decoded_text = bitarray()

with open('compressed_file.bin', 'rb') as r:
    decoded_text.fromfile(r)
    
decoded_text = decoded_text[:-padding] 
    
decoded_text = decoded_text.decode(huffman_dict) 
decoded_text = ''.join(decoded_text)

print(decoded_text)

with open('uncompress.bin', 'w') as w:
    w.write(text)