def array_front9(nums):
    for b in range(4):
        if nums[b]==9:
            return True
    return False

def make_tags(tab, word):
    return '<'+tab+'>'+word+'</'+tab+'>'

#make_tags(gt, mimo)

def extra_end(s):
    if len(s)>=2:
        return 3*(s[(len(s)-2):(len(s))])

#extra_end('string')

def roda2(s):
    if len(s)>=2:
        return s[2:len(s)]+s[0:2]

#roda2('hello')
