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
        seg_adg = set("abcdefg")
        seg_abfg = set("abcdefg")
        for d in patterns:
            if len(d)==2:
                sef_cf = set(d)
            elif len(d)==3:
                seg_acf = set(d)
            elif len(d)==4:
                seg_bcdf = set(d)
            elif len(d)==5:
                seg_adg = seg_adg.intersection(set(d))
            elif len(d)==6:
                seg_abfg = seg_abfg.intersection(set(d))
        return (sef_cf, seg_bcdf, seg_acf, seg_adg, seg_abfg)

    def get_segments_chars(sef_cf, seg_bcdf, seg_acf, seg_adg, seg_abfg):
        # Find a: difference between 7 and 1
        seg_a = seg_acf.difference(sef_cf)
        # Find g: 4+7 are 9-g, the only 6 dig combination with one seg difference  
        seg_g = seg_abfg.difference(seg_adg).difference(sef_cf)      
        # Find c: All 6 seg combinations have f in common
        seg_c = sef_cf.intersection(seg_abfg)
        # Find f: we use dig_1 - seg_c
        seg_f = sef_cf.difference(seg_c)
        # Find e:           
        seg_e = set("abcdefg").difference(seg_abfg).difference(seg_bcdf)
        # Find d: We get d from adg 
        seg_d = seg_adg.difference(seg_a).difference(seg_g)
        # Find d: the one left
        seg_b = seg_bcdf.difference(sef_cf).difference(seg_d)

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
        (sef_cf, seg_bcdf, seg_acf, seg_adg, seg_abfg) = get_masters(patterns)
        (seg_a, seg_b, seg_c, seg_d, seg_e, seg_f, seg_g) = get_segments_chars(sef_cf, seg_bcdf, seg_acf, seg_adg, seg_abfg) 
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
