#!/usr/bin/env python
# encoding: utf-8
"""
util_vietnamese.py

Created by Toan Luu on 2011-07-30.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import util
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
    return BeautifulStoneSoup(category, convertEntities=BeautifulStoneSoup.HTML_ENTITIES).contents[0]    

def tokenized(text):
    pattern = re.compile(r"\W+", re.UNICODE)
    tokens = []
    for token in pattern.split(text):
        if token is not None and len(token) > 0: tokens.append(token)
    return tokens

def simpleTokenized(text):
    pattern = re.compile("[ \-\t\n,]")
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
    tokens = tokenized(text)
    return ' '.join(tokens)

def norm_name(text, maxlen = 12):
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
    
if __name__ == '__main__':
    main()

