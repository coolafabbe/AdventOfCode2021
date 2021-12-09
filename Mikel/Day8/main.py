import os
path = os.path.dirname(os.path.realpath(__file__))

def decode_1(data:list):
    count = 0
    for (patterns, digits) in data:
        for d in digits:
            if len(d) in [2,3,4,7]:
                count += 1
    return count


def decode_2(data:list):

    def get_masters(patterns:list):
        dig_1 = ''
        dig_4 = ''
        dig_7 = ''
        dig_8 = ''
        opt_5 = []
        opt_6 = []
        for d in patterns:
            if len(d)==2:
                dig_1 = d
            elif len(d)==3:
                dig_7 = d
            elif len(d)==4:
                dig_4 = d
            elif len(d)==5:
                if d not in opt_5: opt_5.append(d)
            elif len(d)==6:
                if d not in opt_6: opt_6.append(d)
            elif len(d)==7:
                dig_8 = d
        return (dig_1, dig_4, dig_7, dig_8, opt_5, opt_6)

    def get_segments_chars(dig_1, dig_4, dig_7, dig_8, opt_5, opt_6):
        # Find a: difference between 7 and 1
        seg_a = set(dig_7).difference(set(dig_1))
        assert len(seg_a)==1, print(dig_7,dig_1)
        # Find g: 4+7 are 9-g, the only 6 dig combination with one seg difference  
        # Find c: All 6 seg combinations have f in common
        comb_6 = set("abcdefg")
        almost_dig_9 = set(dig_7).union(set(dig_4))
        for opt in opt_6:
            comb_6 = comb_6.intersection(set(opt))
            diff = set(opt).difference(almost_dig_9)
            if len(diff)==1:
                seg_g = set(diff)
        for c in set(dig_1):
            if c not in comb_6:
                seg_c = set(c)
                break        
        # Find f: we use dig_1 - seg_c
        seg_f = set(dig_1).difference(seg_c)
        # Find e:           
        seg_e = set(dig_8).difference(almost_dig_9.union(seg_g))
        # Find b: We get abg from the opt_5
        seg_adg = set("abcdefg")
        for opt in opt_5:
            seg_adg = seg_adg.intersection(set(opt))
        seg_d = seg_adg.difference(seg_a).difference(seg_g)
        # Find d: the one left
        seg_b = set(dig_4).difference(set(dig_1)).difference(seg_d)

        return (seg_a.pop(), seg_b.pop(), seg_c.pop(), seg_d.pop(), seg_e.pop(), seg_f.pop(), seg_g.pop())

    def get_digits_dict(seg_a, seg_b, seg_c, seg_d, seg_e, seg_f, seg_g):
        res = {}
        res[0] = set(seg_a+seg_b+seg_c+seg_e+seg_f+seg_g)
        res[1] = set(seg_c+seg_f)
        res[2] = set(seg_a+seg_c+seg_d+seg_e+seg_g)
        res[3] = set(seg_a+seg_c+seg_d+seg_f+seg_g)
        res[4] = set(seg_b+seg_c+seg_d+seg_f)
        res[5] = set(seg_a+seg_b+seg_d+seg_f+seg_g)
        res[6] = set(seg_a+seg_b+seg_d+seg_e+seg_f+seg_g)
        res[7] = set(seg_a+seg_c+seg_f)
        res[8] = set(seg_a+seg_b+seg_c+seg_d+seg_e+seg_f+seg_g)
        res[9] = set(seg_a+seg_b+seg_c+seg_d+seg_f+seg_g)
        return res

    count = 0
    for (patterns, digits) in data:
        (dig_1, dig_4, dig_7, dig_8, opt_5, opt_6) = get_masters(patterns)
        (seg_a, seg_b, seg_c, seg_d, seg_e, seg_f, seg_g) = get_segments_chars(dig_1, dig_4, dig_7, dig_8, opt_5, opt_6) 
        digits_dict = get_digits_dict(seg_a, seg_b, seg_c, seg_d, seg_e, seg_f, seg_g)
        number = 0
        for digit in digits:
            number *= 10
            for value, code in digits_dict.items():
                if code == set(digit):
                    number += value
                    break
        count += number
    return count
    

def process_data(data:list):
    res = []
    for l in data:
        [patterns,digits] = l.strip().split(" | ")
        patterns = patterns.split(" ")
        digits = digits.split(" ") 
        res.append((patterns, digits))
    return res

test_data = [
    "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
]
    
test_data_2 = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]

with open(path+"/input.txt") as file:
    data = file.readlines()


assert decode_1(process_data(test_data)) == 26, "Function is wrong"
print("Part A:", decode_1(process_data(data)))
assert decode_2(process_data(test_data_2)) == 5353, "Function is wrong"
assert decode_2(process_data(test_data)) == 61229, "Function is wrong"
print("Part B:", decode_2(process_data(data)))
