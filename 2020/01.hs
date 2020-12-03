-- Advent of Code 2020 Day 1
-- By: Scoder12
-- License: AGPL

module Main where

import qualified Data.Set as Set
import qualified Data.Map as Map
import Utils

main = do
    inputString <- getContents ;
    putStrLn (part1 inputString) ;
    putStrLn (part2 inputString)

parseInp :: String -> [Integer]
parseInp inp = getInts (wordsWhen (=='\n') inp)

find2020num' :: [Integer] -> Set.Set Integer -> Maybe Integer
find2020num' [] possible = Nothing
find2020num' (x:xs) possible = 
    if Set.member x possible then
        Just (x * (2020 - x))
    else
        if x < 2020 then
            find2020num' xs (Set.insert (2020 - x) possible)
        else
            find2020num' xs possible

find2020num :: [Integer] -> Maybe Integer
find2020num inp = find2020num' inp Set.empty

part1 :: String -> String
part1 s = case find2020num (parseInp s) of
    Nothing -> "Error"
    Just result -> show result

findB :: Integer -> [Integer] -> Map.Map Integer Integer -> Set.Set Integer -> (Map.Map Integer Integer, Set.Set Integer)
findB x [] possibleBMap possibleB = (possibleBMap, possibleB)
findB x (y:ys) possibleBMap possibleB = do
    if x < y then
        let z = y - x
            newPossibleB = Set.insert z possibleB
            newPossibleBMap = Map.insert z y possibleBMap
        in findB x ys newPossibleBMap newPossibleB
    else
        findB x ys possibleBMap possibleB


find2020triplet' :: Set.Set Integer -> Map.Map Integer Integer -> Set.Set Integer -> [Integer] -> Maybe (Integer, Integer, Integer)
find2020triplet' possibleA possibleBMap possibleB [] = Nothing
find2020triplet' possibleA possibleBMap possibleB (x:xs) = do
    if Set.member x possibleB then
        Map.lookup x possibleBMap >>= \a1 ->
        let a = 2020 - a1
            b = x
            c = 2020 - (a + b)
        in Just (a, b, c)
    else
        if x < 2020 then
            let newPossibleA = Set.insert (2020 - x) possibleA
                (newPossibleBMap, newPossibleB) = findB x (Set.elems newPossibleA) possibleBMap possibleB
            in find2020triplet' newPossibleA newPossibleBMap newPossibleB xs
        else
            find2020triplet' possibleA possibleBMap possibleB xs

find2020triplet :: [Integer] -> Maybe (Integer, Integer, Integer)
find2020triplet = find2020triplet' Set.empty Map.empty Set.empty

part2 :: String -> String
part2 s = case find2020triplet (parseInp s) of
    Nothing -> "Error"
    Just (a, b, c) -> show (a * b * c)
