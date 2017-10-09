#!/usr/bin/env python
# encoding: utf-8
"""
util_vietnamese.py

Created by Toan Luu on 2011-07-30.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import re
import unicodedata
from BeautifulSoup import BeautifulStoneSoup

def folding(s):
    s = re.sub(u'Đ', 'D', s)
    s = re.sub(u'đ', 'd', s)
    #Normal form D (NFD) is also known as canonical decomposition, and translates each character into its decomposed form
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

#convert to unsign text
def convert2Unsign(text):
    return folding(unicode(text))

# &#361; => "ũ"
def decodeHtml(text):
    return BeautifulStoneSoup(text, convertEntities=BeautifulStoneSoup.HTML_ENTITIES).contents[0]

def tokenized(text):
    pattern = re.compile(r"\W+", re.UNICODE)
    tokens = []
    for token in pattern.split(text):
        if token is not None and len(token) > 0: tokens.append(token)
    return tokens

def simpleTokenized(text):
    pattern = re.compile("[ ,\-\t\n\r]")
    tokens = []
    for token in pattern.split(text.lower()):
        if token is not None and len(token) > 0: tokens.append(token)
    return tokens

# Cong hoa xa hoi chu nghia viet nam => [cong_hoa, xa_hoi, chu_nghia, viet_nam]
def makeCoumpoundTokens(text, nounSet):
    results = []
    tokens = tokenized(text.lower())
    #TODO: if text ="cong hoa, xa hoi" then should not combile "hoa xa", compound > 2 tokens...
    for i in range(0, len(tokens) - 1):
        compound = tokens[i] + ' ' + tokens[i + 1]
        if compound in nounSet: results.append(compound.replace(' ', '_'))
    return results

def makePhraseToken(text):
    tokens = tokenized(text.lower())
    return '_' + '_'.join(tokens)

def makePrefixNGramTokenWithBlacklist(text, nums, blacklist):
    ngrams = []
    tokens = tokenized(text.lower())
    if blacklist is None:
        blacklist = set()
    while len(tokens) > 1 and ('_' + tokens[0]) in blacklist:
        del tokens[0]

    start = 0
    done = False
    while not done:
        done = True
        for numTokens in nums:
            if len(tokens) >= numTokens + start:
                ngram = '_' + '_'.join(tokens[start: start + numTokens])
                # if ngram is blacklisted then we reset at new start
                if blacklist is not None and ngram in blacklist:
                    ngrams = []
                    start = start + numTokens
                    done = False
                    break
                else:
                    ngrams.append(ngram)
    return ngrams

def makePrefixNGramToken(text, nums):
    ngrams = []
    tokens = tokenized(text.lower())
    for numTokens in nums:
        if len(tokens) >= numTokens:
            ngrams.append('_' + '_'.join(tokens[0: numTokens]))
    return ngrams

def makeSlidingNgrams(normText, minTokens, maxTokens):
    tokens = normText.split(' ')
    numTokens = len(tokens)
    if numTokens < minTokens: return []
    results = []
    for l in range(minTokens, maxTokens + 1):
        for i in range(0, numTokens - l + 1):
            results.append(' '.join(tokens[i:i+l]))
    return results

def makeMapNgrams(text, minTokens, maxTokens):
    tokens = tokenized(text.lower())
    numTokens = len(tokens)
    if numTokens < minTokens: return {}

    results = {}
    for l in range(minTokens, maxTokens + 1):
        results[l] = []
        for i in range(0, numTokens - l + 1):
            results[l].append(' '.join(tokens[i:i+l]))
    return results

def makeListNgrams(text, minTokens, maxTokens):
    tokens = tokenized(text.lower())
    numTokens = len(tokens)
    if numTokens < minTokens: return []
    results = []
    for l in range(minTokens, maxTokens + 1):
        for i in range(0, numTokens - l + 1):
            results.append(' '.join(tokens[i:i+l]))
    return results

def makeSlidingNgramsByPriority(norm, minTokens, maxTokens):
    sliding_ngrams = []
    generated_ngrams = makeSlidingNgrams(norm, minTokens, maxTokens)
    current_ngram_length = 1
    current_ngram_list = []
    for index, ngram in enumerate(generated_ngrams):
        if len(ngram.split(' ')) == current_ngram_length:
            current_ngram_list.append(ngram)
        else:
            sliding_ngrams = current_ngram_list + sliding_ngrams
            current_ngram_length += 1
            current_ngram_list = [ngram]
        if index == len(generated_ngrams) - 1:
            sliding_ngrams = current_ngram_list + sliding_ngrams

    return sliding_ngrams

REMOVED_NAME_CHARS = set([u'»', '.', ' ', '\t', '\n', '\r'])

def cleanedName(name):
    end = len(name) - 1
    removed = False
    while end > 0 and name[end] in REMOVED_NAME_CHARS:
        # print 'Remove:', name[end]
        end -= 1
        removed = True
    if removed: name = name[0: end + 1]

    begin = 0
    removed = False
    while begin < len(name) and name[begin] in REMOVED_NAME_CHARS:
        # print 'Remove:', name[begin]
        begin += 1
        removed = True
    if removed: name = name[begin: len(name)]

    # print 'Begin_End:[%s][%s]' % (name[0], name[-1])
    return name

def makeNGramToken(text):
    ngrams = set()
    pattern = re.compile(r"\W+", re.UNICODE)
    tokens = pattern.split(text.lower())
    maxlen = len(tokens)
    if maxlen > 4: maxlen = 4
    for n in range(1,  maxlen + 1):
        for k in range(0, len(tokens) - n + 1):
            ngram = '_' + '_'.join(tokens[k: k + n])
            ngrams.add(ngram)
    return ngrams

# create ngram, plus unsigned
# "lưu vĩnh toàn" = "lưu_vĩnh_toàn", "vĩnh_toàn", "toàn", "luu_vinh_toan", "vinh_toan", "toan"
def makeSuffixNGramToken(text):
    ngrams = set()
    pattern = re.compile(r"\W+", re.UNICODE)
    tokens = pattern.split(text.lower())
    l = len(tokens)
    for i in range(0, l):
        ngram = '_' + '_'.join(tokens[i:l])
        ngrams.add(ngram)
        ngrams.add(convert2Unsign(ngram))
    return ngrams

def norm(text):
    tokens = tokenized(text.lower())
    return ' '.join(tokens)

def norm_name(text, maxlen = 12):
    tokens = tokenized(text.lower())
    if len(tokens) > maxlen: tokens = tokens[0:maxlen]
    return ' '.join(tokens)

def norm_ngrams(text, maxlen = 12):
    tokens = tokenized(text.lower())
    if len(tokens) > maxlen: tokens = tokens[0:maxlen]
    return ' '.join(tokens)

def main():
    # makeSignMap()
    # print convert2Unsign(u'Thử xem ổn không nhé: Lưu Vĩnh Toàn, Phạm Kim Cương')
    print makeCoumpoundTokens('Cong hoa Xa hoi rat Chu nghia Viet nam he he', set(['cong hoa', 'xa hoi', 'chu nghia', 'viet nam']))
    # print makePhraseToken(u'Lưu    Vĩnh+Toàn, Pham; Kim.Cuong')
    # print makePhraseToken(u'Toàn')
    print '========all ngrams:'
    for ngram in makeNGramToken(u'Lưu    Vĩnh+Toàn, Pham; Kim.Cuong'):
        print ngram
    # print '========prefix ngrams:'
    # for ngram in makeSuffixNGramToken(u'Lưu    Vĩnh+Toàn, Pham; Kim.Cuong'):
    #     print ngram
    print 'Folding:', folding((u'Lưu    Vĩnh+Toàn, Pham; Kim.Cuong'))
    print makeMapNgrams('a.b+c-d')

if __name__ == '__main__':
    main()

