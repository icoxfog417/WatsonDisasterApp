import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from app.apis import watson
from app.model.priority import Priority
from app.model.category import Category


class TestWatson(unittest.TestCase):

    def test_priority_watson(self):
        test_data_list = {"High"  :"細かいが重要な案件。要窓口。 @tsuda 「震災後入れ歯洗浄剤・・困っている。孤立した高齢者の方が洗浄"
                                   "しない状況で暮ら・・雑菌が肺に入りやすくそれが原因で亡く・・が増えている。行政に要望・・こういう細"
                                   "かい物資要請はなかなか通らない」（二本松市・歯科技工士） #fumbaro",
                          "Middle":"震災の混乱から約3日、避難所の物資要請が多様化してきた　TLにも各種お知らせが回ってきて、その中に生"
                                   "理用品セールスアカウントからの「生理用品が足りません、お願いします」というものがRTされ、俺も公式R"
                                   "Tしたところ、そのアカウントにフォローされ、ちょっと恥ずかしくなったなあ・・・",
                           "Low"  :"猫ウルフの支援要請（コジキ）リスト http://www.amazon.co.jp/registry/wishlist/1J4I84K1DF1"
                                   "BR/ref=cm_sw_r_tw_ws_P9Etwb01AEA66 … 誰か・・・援助してくれてもええんやで・・・・・・ _:"
                                   "(´ཀ`」 ∠):_"
        }
        priority_test = watson.judge_priority(test_data_list["High"])
        self.assertEqual(priority_test, Priority.High, msg="Miss High")
        priority_test = watson.judge_priority(test_data_list["Middle"])
        self.assertEqual(priority_test, Priority.Middle, msg="Miss Middle")
        priority_test = watson.judge_priority(test_data_list["Middle"])
        self.assertEqual(priority_test, Priority.Middle, msg="Miss Middle")

    def test_category_watson(self):
        category_test = watson.judge_category("ほげほげ")
        print(category_test)
        self.assertNotEqual(category_test, Category.NoSetting)

if __name__ == '__main__':
    unittest.main()
