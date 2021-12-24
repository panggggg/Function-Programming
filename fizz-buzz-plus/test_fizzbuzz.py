import unittest

from fizz_buzz import fizz_buzz_plus

class TestFizzBuzzPluss(unittest.TestCase):
    def test_push_1_should_return_1(self):
        expected = 1
        actual = fizz_buzz_plus(number=1)
        self.assertEquals(expected, actual)

    def test_push_3_should_return_fizz(self):
        expected = "fizz"
        actual = fizz_buzz_plus(number=3)
        self.assertEquals(expected, actual)

    def test_push_5_should_return_buzz(self):
        expected = "buzz"
        actual = fizz_buzz_plus(number=5)
        self.assertEquals(expected, actual)

    def test_push_7_should_return_bizz(self):
        expected = "bizz"
        actual = fizz_buzz_plus(number=7)
        self.assertEquals(expected, actual)

    def test_push_11_should_return_bazz(self):
        expected = "bazz"
        actual = fizz_buzz_plus(number=11)
        self.assertEquals(expected, actual)

    def test_push_13_should_return_boom(self):
        expected = "boom"
        actual = fizz_buzz_plus(number=13)
        self.assertEquals(expected, actual)

    def test_push_17_should_return_bing(self):
        expected = "bing"
        actual = fizz_buzz_plus(number=17)
        self.assertEquals(expected, actual)

    def test_push_19_should_return_bang(self):
        expected = "bang"
        actual = fizz_buzz_plus(number=19)
        self.assertEquals(expected, actual)
    
    def test_push_23_should_return_bong(self):
        expected = "bong"
        actual = fizz_buzz_plus(number=23)
        self.assertEquals(expected, actual)

    def test_push_29_should_return_fozz(self):
        expected = "fozz"
        actual = fizz_buzz_plus(number=29)
        self.assertEquals(expected, actual)

    def test_push_31_should_return_fazz(self):
        expected = "fazz"
        actual = fizz_buzz_plus(number=31)
        self.assertEquals(expected, actual)

    def test_push_37_should_return_woof(self):
        expected = "woof"
        actual = fizz_buzz_plus(number=37)
        self.assertEquals(expected, actual)

    def test_push_15_should_return_fizzbuzz(self):
        expected = "fizzbuzz"
        actual = fizz_buzz_plus(number=15)
        self.assertEquals(expected, actual)

    def test_push_21_should_return_fizzbizz(self):
        expected = "fizzbizz"
        actual = fizz_buzz_plus(number=21)
        self.assertEquals(expected, actual)

    def test_push_35_should_return_buzzbizz(self):
        expected = "buzzbizz"
        actual = fizz_buzz_plus(number=35)
        self.assertEquals(expected, actual)

    def test_push_35_should_return_buzzbizz(self):
        expected = "buzzbizz"
        actual = fizz_buzz_plus(number=35)
        self.assertEquals(expected, actual)

    def test_push_105_should_return_fizzbuzzbizz(self):
        expected = "fizzbuzzbizz"
        actual = fizz_buzz_plus(number=105)
        self.assertEquals(expected, actual)

    def test_push_33_should_return_fizzbazz(self):
        expected = "fizzbazz"
        actual = fizz_buzz_plus(number=33)
        self.assertEquals(expected, actual)
    
    def test_push_55_should_return_buzzbazz(self):
        expected = "buzzbazz"
        actual = fizz_buzz_plus(number=55)
        self.assertEquals(expected, actual)

    def test_push_77_should_return_bizzbazz(self):
        expected = "bizzbazz"
        actual = fizz_buzz_plus(number=77)
        self.assertEquals(expected, actual)

    def test_push_165_should_return_fizzbuzzbazz(self):
        expected = "fizzbuzzbazz"
        actual = fizz_buzz_plus(number=165)
        self.assertEquals(expected, actual)

    def test_push_385_should_return_buzzbizzbazz(self):
        expected = "buzzbizzbazz"
        actual = fizz_buzz_plus(number=385)
        self.assertEquals(expected, actual)

    def test_push_1155_should_return_fizzbuzzbizzbazz(self):
        expected = "fizzbuzzbizzbazz"
        actual = fizz_buzz_plus(number=1155)
        self.assertEquals(expected, actual)
    
    def test_push_39_should_return_fizzboom(self):
        expected = "fizzboom"
        actual = fizz_buzz_plus(number=39)
        self.assertEquals(expected, actual)

    def test_push_65_should_return_buzzboom(self):
        expected = "buzzboom"
        actual = fizz_buzz_plus(number=65)
        self.assertEquals(expected, actual)

    def test_push_91_should_return_bizzboom(self):
        expected = "bizzboom"
        actual = fizz_buzz_plus(number=91)
        self.assertEquals(expected, actual)

    def test_push_143_should_return_bazzboom(self):
        expected = "bazzboom"
        actual = fizz_buzz_plus(number=143)
        self.assertEquals(expected, actual)

    def test_push_195_should_return_fizzbuzzboom(self):
        expected = "fizzbuzzboom"
        actual = fizz_buzz_plus(number=195)
        self.assertEquals(expected, actual)

    def test_push_273_should_return_fizzbizzboom(self):
        expected = "fizzbizzboom"
        actual = fizz_buzz_plus(number=273)
        self.assertEquals(expected, actual)

    def test_push_429_should_return_fizzbazzboom(self):
        expected = "fizzbazzboom"
        actual = fizz_buzz_plus(number=429)
        self.assertEquals(expected, actual)

    def test_push_455_should_return_buzzbizzboom(self):
        expected = "buzzbizzboom"
        actual = fizz_buzz_plus(number=455)
        self.assertEquals(expected, actual)

    def test_push_715_should_return_buzzbazzboom(self):
        expected = "buzzbazzboom"
        actual = fizz_buzz_plus(number=715)
        self.assertEquals(expected, actual)

    def test_push_1001_should_return_bizzbazzboom(self):
        expected = "bizzbazzboom"
        actual = fizz_buzz_plus(number=1001)
        self.assertEquals(expected, actual)

    def test_push_1365_should_return_fizzbuzzbizzboom(self):
        expected = "fizzbuzzbizzboom"
        actual = fizz_buzz_plus(number=1365)
        self.assertEquals(expected, actual)

    def test_push_2145_should_return_fizzbuzzbazzboom(self):
        expected = "fizzbuzzbazzboom"
        actual = fizz_buzz_plus(number=2145)
        self.assertEquals(expected, actual)

    def test_push_5005_should_return_buzzbizzbazzboom(self):
        expected = "buzzbizzbazzboom"
        actual = fizz_buzz_plus(number=5005)
        self.assertEquals(expected, actual)

    def test_push_15015_should_return_fizzbuzzbizzbazzboom(self):
        expected = "fizzbuzzbizzbazzboom"
        actual = fizz_buzz_plus(number=15015)
        self.assertEquals(expected, actual)

    def test_push_561_should_return_fizzbazzbing(self):
        expected = "fizzbazzbing"
        actual = fizz_buzz_plus(number=561)
        self.assertEquals(expected, actual)

    def test_push_255255_should_return_fizzbuzzbizzbazzboombing(self):
        expected = "fizzbuzzbizzbazzboombing"
        actual = fizz_buzz_plus(number=255255)
        self.assertEquals(expected, actual)

    def test_push_1045_should_return_buzzbazzbang(self):
        expected = "buzzbazzbang"
        actual = fizz_buzz_plus(number=1045)
        self.assertEquals(expected, actual)

    def test_push_4849845_should_return_fizzbuzzbizzbazzboombingbang(self):
        expected = "fizzbuzzbizzbazzboombingbang"
        actual = fizz_buzz_plus(number=4849845)
        self.assertEquals(expected, actual)

    def test_push_391_should_return_bingbong(self):
        expected = "bingbong"
        actual = fizz_buzz_plus(number=391)
        self.assertEquals(expected, actual)

    def test_push_6555_should_return_fizzbuzzbangbong(self):
        expected = "fizzbuzzbangbong"
        actual = fizz_buzz_plus(number=6555)
        self.assertEquals(expected, actual)

    def test_push_111546435_should_return_fizzbuzzbizzbazzboombingbangbong(self):
        expected = "fizzbuzzbizzbazzboombingbangbong"
        actual = fizz_buzz_plus(number=111546435)
        self.assertEquals(expected, actual)
    
    def test_push_6061_should_return_bazzbangfozz(self):
        expected = "bazzbangfozz"
        actual = fizz_buzz_plus(number=6061)
        self.assertEquals(expected, actual)
    
    def test_push_3234846615_should_return_fizzbuzzbizzbazzboombingbangbongfozz(self):
        expected = "fizzbuzzbizzbazzboombingbangbongfozz"
        actual = fizz_buzz_plus(number=3234846615)
        self.assertEquals(expected, actual)

    def test_push_67735_should_return_buzzbangbongfazz(self):
        expected = "buzzbangbongfazz"
        actual = fizz_buzz_plus(number=67735)
        self.assertEquals(expected, actual)

    def test_push_100280245065_should_return_fizbuzzbizzbazzboombingbangbongfozzfazz(self):
        expected = "fizzbuzzbizzbazzboombingbangbongfozzfazz"
        actual = fizz_buzz_plus(number=100280245065)
        self.assertEquals(expected, actual)
    
    def test_push_54723_should_return_fizzbingfozzwoof(self):
        expected = "fizzbingfozzwoof"
        actual = fizz_buzz_plus(number=54723)
        self.assertEquals(expected, actual)

    def test_push_3710369067405_should_return_fizzbuzzbizzbazzboombingbangbongfozzfazzwoof(self):
        expected = "fizzbuzzbizzbazzboombingbangbongfozzfazzwoof"
        actual = fizz_buzz_plus(number=3710369067405)
        self.assertEquals(expected, actual)