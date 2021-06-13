{-# Language DeriveDataTypeable #-}
-- Advent of Code 2020 Day 1
-- By: Scoder12
-- License: AGPL

module Main where

import           Data.Data                      ( Data
                                                , Typeable
                                                )
import           Data.Maybe
import           Utils

main = do
  inputString <- getContents
  let parsed = parseInput inputString
  putStrLn (part1 parsed)
  putStrLn (part2 parsed)

data Direction = Tree | Air deriving (Eq, Show, Data, Typeable)
type Row = [Direction]
type Course = [Row]


parseLine :: String -> Row
parseLine s = [ if c == '#' then Tree else Air | c <- s ]

parseInput :: String -> Course
parseInput s = map parseLine (wordsWhen (== '\n') s)

countTrees' :: Course -> Int -> Int -> Int -> Int -> Int -> Int -> Int
countTrees' m right down x y trees width = if y < length m
  then
    let newTress =
          if ((m !! y) !! (x `mod` width)) == Tree then trees + 1 else trees
    in  countTrees' m right down (x + right) (y + down) newTress width
  else trees

countTrees :: Course -> Int -> Int -> Int
countTrees m right down = countTrees' m right down 0 0 0 $ length $ head m

part1 :: Course -> String
part1 m = show $ countTrees m 3 1

part2 :: Course -> String
part2 m =
  show
    $ countTrees m 1 1
    * countTrees m 3 1
    * countTrees m 5 1
    * countTrees m 7 1
    * countTrees m 1 2
