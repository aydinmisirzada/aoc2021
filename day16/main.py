from queue import Queue

hex_to_binary = {
'0' : '0000',
'1' : '0001',
'2' : '0010',
'3' : '0011',
'4' : '0100',
'5' : '0101',
'6' : '0110',
'7' : '0111',
'8' : '1000',
'9' : '1001',
'A' : '1010',
'B' : '1011',
'C' : '1100',
'D' : '1101',
'E' : '1110',
'F' : '1111',
}

def load_data(src):
    with open(src,'r') as f:
        line = f.readline().strip()
        
    return line

def convert_to_binary(line):
    result = ''
    for c in line:
        result += hex_to_binary[c]
    
    q = Queue()
    for b in result:
        q.put_nowait(b)

    return q

class Packet:
    def __init__(self,
                version,
                type_id,
                value = None,
                subpackets = None):

        self.version = int(version,2)
        self.type_id = int(type_id,2)
        self.value = value
        self.subpackets = subpackets
    
    def set_value(self,value):
        if self.type_id == 4:
            self.value = int(value,2)
        else:
            raise ValueError('This packet is not of literal type')

    def __repr__(self):
        rep = 'Version: '+str(self.version)+'\nType: '+str(self.type_id)
        if self.value:
            rep += '\nValue: '+str(self.value)
        if self.subpackets:
            rep += '\nNum of Subpackets: '+str(len(self.subpackets))
            
            for packet in self.subpackets:
                rep += '\n\n'+repr(packet)
        return rep

def pop_str(bits: Queue,count=3):
    l = []
    for _ in range(count):
        l.append(bits.get_nowait())

    return ''.join(l)

def pop_bits(bits: Queue,count=3):
    res = Queue()
    for _ in range(count):
        res.put_nowait(bits.get_nowait())

    return res

def read_packet(bits: Queue):
    """
    >>> p = read_packet(convert_to_binary("EE00D40C823060"))
    >>> print(p.subpackets[0].value)
    1
    >>> p = read_packet(convert_to_binary("8A004A801A8002F478"))
    >>> print(p.version)
    4
     >>> p = read_packet(convert_to_binary("620080001611562C8802118E34"))
    >>> print(p.version)
    3
    """

    version = pop_str(bits,3)
    type_id = pop_str(bits,3)

    if int(type_id,2) == 4: #read value
        value = ''
        while True:
            tmp = pop_str(bits,5)
            group_value = tmp[1:]
            value += group_value
            if tmp[0] == '0':
                break
        value = int(value,2)

        return Packet(version, type_id, value=value)
    else: #read inside the operator packet
        length_type_id = bits.get_nowait()
        subpackets = []

        if length_type_id == '0':
            length_in_bits = pop_str(bits,15)
            length = int(length_in_bits,2)

            next_bits = pop_bits(bits, length)

            while not next_bits.empty():
                packet = read_packet(next_bits)
                subpackets.append(packet)
            
        else:
            num_in_bits = pop_str(bits,11)
            num = int(num_in_bits,2)

            for _ in range(num):
                packet = read_packet(bits)
                subpackets.append(packet)

        return Packet(version, type_id, subpackets=subpackets)
    
def star1(bits: Queue):
    """
    >>> q = convert_to_binary("8A004A801A8002F478")
    >>> print(star1(q))
    16
    """

    root = read_packet(bits)

    sum_version = 0
    buffer = [root]

    while buffer:
        packet = buffer.pop()
        sum_version += packet.version

        if packet.type_id != 4:
            buffer += packet.subpackets

    return sum_version


if __name__ == '__main__':
    data = load_data('data.txt')
    q = convert_to_binary(data)

    result = star1(q)
    print(result)