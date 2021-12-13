import os
import numpy as np


def get_paths(lines:list, alternative:bool=False):

    def process_lines(lines:list):
        nodes = {'start':set(), 'end':set()}
        for line in lines:
            node1, node2 = line.split('-')
            if node1 not in nodes:
                nodes[node1] = set()
            if node2 not in nodes:
                nodes[node2] = set()
            if node1 != 'end' and node2 != 'start':
                nodes[node1].update({node2})
            if node2 != 'end' and node1 != 'start':
                nodes[node2].update({node1})
        return nodes
    
    def check_exists(paths, path):
        for p in paths:
            if p == path:
                return True
        return False

    def build_path(nodes, paths, path, alternative):
        if path[-1] in path[:-1]:
            if path[-1].islower():
                if not alternative:
                    return
                else:
                    if '**' in path:
                        return
                    else:
                        path = ['**'] + path

        if path[-1] == 'end':
            if not check_exists(paths, path):
                paths.append(path)
            return
        for n in nodes[path[-1]]:
            build_path(nodes, paths, path+[n], alternative)

    def calc_paths(nodes:dict, alternative:bool=False):
        paths = []
        for n in nodes['start']:
            build_path(nodes, paths, ['start', n], alternative)
        return paths

    nodes = process_lines(lines)
    paths = calc_paths(nodes, alternative)
    count = len(paths)
    return count
            

test_lines1 = [
    'dc-end',
    'HN-start',
    'start-kj',
    'dc-start',
    'dc-HN',
    'LN-dc',
    'HN-end',
    'kj-sa',
    'kj-HN',
    'kj-dc',
]

test_lines2 = [
    'fs-end',
    'he-DX',
    'fs-he',
    'start-DX',
    'pj-DX',
    'end-zg',
    'zg-sl',
    'zg-pj',
    'pj-he',
    'RW-he',
    'fs-DX',
    'pj-RW',
    'zg-RW',
    'start-pj',
    'he-WI',
    'zg-he',
    'pj-fs',
    'start-RW',
]

lines = [
    'QR-da',
    'QR-end',
    'QR-al',
    'start-op',
    'zh-iw',
    'zh-start',
    'da-PF',
    'op-bj',
    'iw-QR',
    'end-HR',
    'bj-PF',
    'da-LY',
    'op-PF',
    'bj-iw',
    'end-da',
    'bj-zh',
    'HR-iw',
    'zh-op',
    'zh-PF',
    'HR-bj',
    'start-PF',
    'HR-da',
    'QR-bj',
]


assert get_paths(test_lines1) == 19, "Function is wrong"
assert get_paths(test_lines2) == 226, "Function is wrong"
print("Part A:", get_paths(lines))
assert get_paths(test_lines1, alternative=True) == 103, "Function is wrong"
assert get_paths(test_lines2, alternative=True) == 3509, "Function is wrong"
print("Part B:", get_paths(lines, alternative=True))
