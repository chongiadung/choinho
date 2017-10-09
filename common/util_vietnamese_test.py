#!/usr/bin/env python
# encoding: utf-8
import unittest
from common import util_vietnamese as uv
        
class TestUtilVietnamese(unittest.TestCase):
        
    def testConvert2Unsign(self):
        self.assertEquals(uv.convert2Unsign(u'Dĩ độc trị độc'), u'Di doc tri doc')
        self.assertEquals(uv.convert2Unsign(u'Ông ăn ổi Ạ'), u'Ong an oi A')
        self.assertEquals(uv.convert2Unsign(u'Giầy thể thao nữ'), u'Giay the thao nu')
        self.assertEquals(uv.convert2Unsign(u'Thử xem ổn không nhé: Lưu Vĩnh Toàn, Phạm Kim Cương'), u'Thu xem on khong nhe: Luu Vinh Toan, Pham Kim Cuong')
        
    def testTokenized(self):
        s = u'Lưu    Vĩnh+Toàn,   Pham; Kim.Cuong A-B. A_B'
        expect = [u'Lưu', u'Vĩnh', u'Toàn', u'Pham', u'Kim', u'Cuong', u'A', u'B', 'A_B']
        self.assertEquals(uv.tokenized(s), expect)
        
    def testMakePhraseToken(self):
        self.assertEquals(uv.makePhraseToken(u'Lưu    Vĩnh+Toàn, Pham; Kim.Cuong'), u'_lưu_vĩnh_toàn_pham_kim_cuong')
        self.assertEquals(uv.makePhraseToken(u'Toàn'), u'_toàn')
        self.assertEquals(uv.makePhraseToken(u';'), u'__')
        self.assertEquals(uv.makePhraseToken(u''), u'_')
    
    def testMakeSuffixNGramToken(self):
        expect = set()
        expect.add(u'_lưu_vĩnh_toàn_pham_kim_cuong')
        expect.add(u'_luu_vinh_toan_pham_kim_cuong')
        expect.add(u'_vĩnh_toàn_pham_kim_cuong')
        expect.add(u'_vinh_toan_pham_kim_cuong')
        expect.add(u'_toàn_pham_kim_cuong')
        expect.add(u'_toan_pham_kim_cuong')
        expect.add(u'_pham_kim_cuong')
        expect.add(u'_kim_cuong')
        expect.add(u'_cuong')
        self.assertEquals(uv.makeSuffixNGramToken(u'Lưu    Vĩnh+Toàn, Pham; Kim.Cuong'), expect)
        
    def testMakeNGramToken(self):
        expect = set()
        expect.add(u'_lưu_vĩnh_toàn_pham')
        expect.add(u'_vĩnh_toàn_pham_kim')
        expect.add(u'_toàn_pham_kim_cuong')
        expect.add(u'_lưu_vĩnh_toàn')
        expect.add(u'_vĩnh_toàn_pham')
        expect.add(u'_toàn_pham_kim')
        expect.add(u'_pham_kim_cuong')
        expect.add(u'_lưu_vĩnh')
        expect.add(u'_vĩnh_toàn')
        expect.add(u'_toàn_pham')
        expect.add(u'_pham_kim')
        expect.add(u'_kim_cuong')
        expect.add(u'_lưu')
        expect.add(u'_vĩnh')
        expect.add(u'_toàn')
        expect.add(u'_pham')
        expect.add(u'_kim')
        expect.add(u'_cuong')
        
        self.assertEquals(uv.makeNGramToken(u'Lưu    Vĩnh+Toàn, Pham; Kim.Cuong'), expect)
    def testSimpleTokenized(self):
        self.assertEquals(uv.simpleTokenized(u'hello    \tw'), ['hello', 'w'])
        self.assertEquals(uv.simpleTokenized(u't-mobile'), ['t','mobile'])
        self.assertEquals(uv.simpleTokenized(u'o to, xe may'), ['o', 'to','xe', 'may'])
            
if __name__ == '__main__':
    unittest.main()
