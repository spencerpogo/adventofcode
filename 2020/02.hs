-- Advent of Code 2020 Day 1
-- By: Scoder12
-- License: AGPL

module Main where

import Data.Maybe
import Text.Read (readMaybe)
import Utils

main = do
    inpString <- getContents ;
    putStrLn (part1 (parseInp inpString)) ;
    putStrLn (part2 (parseInp inpString))

data PasswordRule = PasswordRule {
    ruleA :: Int,
    ruleB :: Int,
    ruleChar :: Char } deriving (Eq, Ord, Show)

parseInp :: String -> [(PasswordRule, String)]
parseInp s = catMaybes (map parseInp' (wordsWhen (=='\n') s))

parseInp' :: String -> Maybe (PasswordRule, String)
parseInp' line = case wordsWhen (\c -> c == ' ' || c == ':') line of
    [amts, char, testcase] -> (case wordsWhen (=='-') amts of
        [numa, numb] -> (readMaybe numa :: Maybe Int) >>= \a ->
                        (readMaybe numb :: Maybe Int) >>= \b ->
                        Just (PasswordRule { ruleA=a, ruleB=b, ruleChar=(char !! 0) }, testcase)
        otherwise -> Nothing)
    otherwise -> Nothing

validSled :: PasswordRule -> String -> Bool
validSled rule s = 
    let count = countChars s (ruleChar rule)
    in count >= (ruleA rule) && count <= (ruleB rule)

maybeGet :: Ord a => Int -> [a] -> Maybe a
maybeGet ind arr
    | (ind > -1) && (length arr > ind) = Just (arr !! ind)
    | otherwise = Nothing

maybeComp :: Char -> Maybe Char -> Bool
maybeComp a b = (case b of
    Nothing -> False
    Just x -> a == x)

validToboggan :: PasswordRule -> [Char] -> Bool
validToboggan rule s = 
    let rc = (ruleChar rule) :: Char
        a = maybeComp rc $ maybeGet ((ruleA rule) - 1) s
        b = maybeComp rc $ maybeGet ((ruleB rule) - 1) s
    in a /= b

countValid :: [(PasswordRule, String)] -> (PasswordRule -> String -> Bool) -> Int
countValid cases checker = length $ filter (uncurry $ checker) cases

part1 :: [(PasswordRule, String)] -> String
part1 cases = show $ countValid cases validSled

part2 :: [(PasswordRule, String)] -> String
part2 cases = show $ countValid cases validToboggan
