from Tree import Node
def makelist(words):
    wordlist=[]
    #go through each word
    for word in words:

        wordlist.append(word.replace("\n","$"))

    return wordlist


def MSD_radix_string_sort(L, i):

    # base case (list must already be sorted)
    if len(L) <= 1:
        return L

    # divide (first by length, then by lexicographical order of the first character)
    done_bucket = []
    buckets = [ [] for x in range(27) ] # one for each letter in a-z

    for s in L:
        if i >= len(s):
            done_bucket.append(s)
        else:
            buckets[ ord(s[i]) - ord('a') ].append(s)

    # conquer (recursively sort buckets)
    buckets = [ MSD_radix_string_sort(b, i + 1) for b in buckets ]

    # marry (chain all buckets together)
    return done_bucket + [ b for blist in buckets for b in blist ]

def createTrie(sortedlist):
    Trie = Node(None)
    count=0
    substr=""
    currword= sortedList[0]
    for i in range(1,len(sortedlist)):
        if currword[0]==sortedList[i][0]:
            Trie.add_child(currword[0])

    for c in Trie.children:
        print(c.data)

if __name__=='__main__':
    words=open('text.txt')
    wordlist=makelist(words)
    sortedList = MSD_radix_string_sort(wordlist, 0)
    print(sortedList)
    createTrie(sortedList)
