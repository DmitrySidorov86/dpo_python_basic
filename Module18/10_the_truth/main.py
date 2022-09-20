def change_one(simbl):
    for letter in alphabet:
        if simbl == letter:
            return alphabet[(alphabet.index(simbl)-1) % len(alphabet)]


alphabet = '!"#$%&"()*+,-./:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm ' \
       'yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj' \
       ' vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst ' \
       'tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ' \
       'ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf ' \
       'wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh' \
       ' x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ' \
       'ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'
text_simple = text.split(' ')
shift = -3
count = 0
new_text = ['']

for i in text_simple:
    i_list = list(i)

    while count != abs(shift):

        if shift > 0 :
            i_list.append(i_list.pop(0))
        else:
            i_list.insert(0, i_list.pop())

        text_one = ''.join(i_list)
        count += 1

    code_list = [change_one(x) if x in alphabet else " " for x in text_one]
    new_code = "".join(code_list)
    count = 0
    new_text.append(new_code)

    if new_code.endswith('.'):
        shift -= 1
        new_text.append('\n')

print(' '.join(new_text))









