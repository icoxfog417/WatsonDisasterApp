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
                          "Middle" :"震災の混乱から約3日、避難所の物資要請が多様化してきた　TLにも各種お知らせが回ってきて、その中に生"
                                   "理用品セールスアカウントからの「生理用品が足りません、お願いします」というものがRTされ、俺も公式R"
                                   "Tしたところ、そのアカウントにフォローされ、ちょっと恥ずかしくなったなあ・・・",
                           "Low"  :"猫ウルフの支援要請（コジキ）リスト http://www.amazon.co.jp/registry/wishlist/1J4I84K1DF1"
                                   "BR/ref=cm_sw_r_tw_ws_P9Etwb01AEA66 … 誰か・・・援助してくれてもええんやで・・・・・・ _:"
                                   "(´ཀ`」 ∠):_"
        }
        priority_choose = {"High"  : Priority.High,
                           "Middle": Priority.Middle,
                           "Low"   : Priority.Low
                           }
        for key, value in test_data_list.items():
            priority_test = watson.judge_priority(value)
            self.assertEqual(priority_test, priority_choose[key], msg=key)

    def test_category_watson(self):
        test_data_list = {
                    "安否確認" :"妻が家で強盗に襲われたらしい。妻の安否を確認すると持っていた包丁で強盗を撃退したらしい。妻を迎えに警察"
                            "署に行くと、妻は「インターホンが鳴ってあなたかと思って玄関にでたらいきなり襲い掛かってきたの」と言った。私"
                            "は妻を抱きしめながら怖かっただろうとその頭を撫でた。",
                    "物資要請" : "物資が少ない救援物資を要請する",
                    "救助" : "@Flandre9991 当時「エンカウンター」の乗組員であった元英海軍中尉「サミュエル・フォール」は、この救命救助" \
                           "行為を「武士道の実践」と称賛。恩人である工藤艦長の消息を求めて来日した。",
                    "ライフライン" : "RT @perfumekawaee: 橋が崩落し首都のライフラインは麻痺、橋を作った韓国は逃亡、再建する金も無い" \
                               "パラオを助けたのは日本。無料で建設された橋には、日本パラオ友好の記念碑が建てられている　http://t.co/" \
                               "szG6qRWDqK　 http://t.co/hT8…,",
                    "交通機関" : "RT @pstmPR: 「バスが邪魔」とのたまう皆さんは、おそらくこんな風景を見て、バスが邪魔だと思われている" \
                             "のでしょう。しかし公共交通機関でも行けるところにマイカーで行く人がわんさかいた結果、こういう渋滞が起きて" \
                             "いる現実も意識してもらいたいものです。 https://t.co…,",
                    "住宅情報" : "【番組案内】ミサワエムアールディー特約店・プラン建設プレゼンツ「せきちゃんの住まいのアンサー」地下鉄赤" \
                             "塚駅4番出口目の前の不動産会社・プラン建設のせきちゃんとカメのコンビでお送りする住宅エンターテイメント番組" \
                             "！今週も住宅情報を笑いとランキング形式で楽しくご紹介☆ #neribro,",
                    "医療・福祉・健康相談" : "での介護といった((福祉))機能の回復や社会復帰を目指す((リハビリテーション))80歳になって" \
                                   "      も20本の歯を持つ運動((8020運動))45…",
                    "生活支援・相談" : "RT @fp_kyokai: 当協会では、各行政と連携し、修学支援アドバイザーや生活困窮者自立支援制度に基づ" \
                                "く家計相談事業などにFPを派遣中です。＜子供の貧困問題＞放置すれば経済損失２．９兆円　日本財団（毎日新" \
                                "聞）https://t.co/qvQyjiO2Ey https:/…",
                    "NoSetting" : "hogehoge"
        }
        #Confidence
        category_choose = {"安否確認" : Category.LifeConFirmation,
                          "物資要請" : Category.HelpObject,
                          "救助" : Category.AssistantRequest,
                          "ライフライン" : Category.LifeLine,
                          "交通機関" : Category.TransPortation,
                          "住宅情報" : Category.HouseInformation,
                          "医療・福祉・健康相談" : Category.NoSetting,
                          "生活支援・相談" : Category.LifeCareInformation,
                          "NoSetting" : Category.NoSetting
        }

        for key, value in test_data_list.items():
            category_test = watson.judge_category(value)
            self.assertEqual(category_test, category_choose[key], msg=key)

    def test_total_watson(self):
        test_data_list = {"High"  :"細かいが重要な案件。要窓口。 @tsuda 「震災後入れ歯洗浄剤・・困っている。孤立した高齢者の方が洗浄"
                                   "しない状況で暮ら・・雑菌が肺に入りやすくそれが原因で亡く・・が増えている。行政に要望・・こういう細"
                                   "かい物資要請はなかなか通らない」（二本松市・歯科技工士） #fumbaro",
                          "Middle" :"震災の混乱から約3日、避難所の物資要請が多様化してきた　TLにも各種お知らせが回ってきて、その中に生"
                                    "理用品セールスアカウントからの「生理用品が足りません、お願いします」というものがRTされ、俺も公式R"
                                    "Tしたところ、そのアカウントにフォローされ、ちょっと恥ずかしくなったなあ・・・",
                          "Low"  :"猫ウルフの支援要請（コジキ）リスト http://www.amazon.co.jp/registry/wishlist/1J4I84K1DF1"
                                  "BR/ref=cm_sw_r_tw_ws_P9Etwb01AEA66 … 誰か・・・援助してくれてもええんやで・・・・・・ _:"
                                  "(´ཀ`」 ∠):_"
                          }
        priority_choose = {"High"  : Priority.High,
                           "Middle": Priority.Middle,
                           "Low"   : Priority.Low
                           }
        category_choose = {"High"  : Category.HelpObject,
                           "Middle": Category.NoSetting,
                           "Low"   : Category.NoSetting
                           }
        for key, value in test_data_list.items():
            priority_test = watson.judge_priority(value)
            category_test = watson.judge_category(value)
            self.assertEqual(priority_test, priority_choose[key], msg=key)
            self.assertEqual(category_test, category_choose[key], msg=key)

if __name__ == '__main__':
    unittest.main()
