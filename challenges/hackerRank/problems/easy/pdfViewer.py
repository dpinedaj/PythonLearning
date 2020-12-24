
def designerPdfViewer(h, word):
    li = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    d = dict(zip(li,h))
    h = 0
    for letra in word:
        if d[letra]>h:
            h = d[letra]
    
    return((len(word)*int(h)))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)