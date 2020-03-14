#!/usr/bin/env python
# -*- coding: utf-8 -*-

from timeit import timeit
import unittest

from spacechem import level, solution, game
import test_data

class TestGame(unittest.TestCase):
    def test_valid_solutions(self):
        for level_code in test_data.valid_levels_and_solutions:
            level_obj = level.ResearchLevel(level_code)

            for solution_code in test_data.valid_levels_and_solutions[level_code]:
                solution_obj = solution.Solution(solution_code)

                with self.subTest(msg=f'{level_obj.get_name()} {solution_obj.name}'):
                    self.assertEqual(game.score_soln(level_obj, solution_obj),
                                     solution_obj.expected_score)

                    # Check the time performance of the solver
                    avg_time = timeit(lambda: game.score_soln(level_obj, solution_obj),
                                      number=100, globals=globals()) / 100
                    print(f'{level_obj.get_name()} {solution_obj.name} ran in avg {avg_time} seconds')


    def test_infinite_loops(self):
        for level_code, solution_code in test_data.infinite_loops:
            level_obj = level.ResearchLevel(level_code)
            solution_obj = solution.Solution(solution_code)
            with self.subTest(msg=f'{level_obj.get_name()}'):
                with self.assertRaises(game.InfiniteLoopException):
                    game.score_soln(level_obj, solution_obj)


if __name__ == '__main__':
    unittest.main(verbosity=0)
