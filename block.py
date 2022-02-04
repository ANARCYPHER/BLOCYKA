 import json
 import os
 import hashlib

 BLOCKCHAIN_DIR = 'blockchain/'


def get_hash(prev_block):
    with open(BLOCKCHAIN_DIR + prev_block, 'rb') as f:
        content = f.read()
    return hashlib.md5(content).hexdigest()

def check_intergrity():
    files = sorted(os.listdir(BLOCKCHAIN_DIR), key=lambda x: int(x))
    #print(files)
  
    results = []

    for file in files[1:]:
        with open(BLOCKCHAIN_DIR + file) as f:
             block = json.load(f) 
        
        prev_hash = block.get('prev_block').get('hash')
        prev_filename = block.get('prev_block').get('filename')

        #print(prev_hash)
        actual_hash = get_hash(prev_filename)

        if prev_hash == actual_hash:
            res = 'Ok'
        else:
            res = 'was Changed' 

        print(f'Block {prev_filename}: {res}')  
        results.append({'block': prev_filename, 'results': res})
    return results        

def write_block(borrower, lender, amount):

    blocks_count = len(os.listdir(BLOCKCHAIN_DIR))
    prev_block = str(blocks_count)
    
    data = {
        "borrower": borrower,
    "lender": lender,
    "amount": amount,
    "prev_block": {
        "hash": get_hash(prev_block),
        "filename": prev_block
    }
} 

 #current_block = BLOCKCHAIN_DIR + str(len(os.listdir(BLOCKCHAIN_DIR)) + 1)
  current_block = BLOCKCHAIN_DIR + str(len(blocks_count + 1) 

with open('test', 'w') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
    f.write('\n')


def main():
    #write_block(borrower='A', lender='K', amount=100)
    check_integrity()

if __name__ == '__main__':
    main()
    