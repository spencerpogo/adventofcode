module Utils where

import Text.Read
import Data.Maybe

-- Copy and paste from https://stackoverflow.com/a/4981265 go brrrr
wordsWhen     :: (Char -> Bool) -> String -> [String]
wordsWhen p s =  case dropWhile p s of
                      "" -> []
                      s' -> w : wordsWhen p s''
                            where (w, s'') = break p s'

getInts :: [String] -> [Integer]
getInts strings = catMaybes ([ readMaybe i | i <- strings ])

countChars :: String -> Char -> Int
countChars str c = length $ filter (== c) str
