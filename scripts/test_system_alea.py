#!/usr/bin/env python3
import utils.datasets as ds
import utils.mesure as ms
import numpy
import random


def main():
    str0 = ""
    all_usr_funny = []
    all_usr_grade = []

    usr_vid, vid_usr, lusr, lvid = ds.combine_datas()
    del vid_usr
    test_system = ds.usr_specific(usr_vid, lvid, 10)
    for tested_usr in lusr:
        labels_test_funny = ds.list_features(
            test_system, [tested_usr], "test", lvid, "funny")
        labels_test_grade = ds.list_features(
            test_system, [tested_usr], "test", lvid, "grade")
        pred_funny, pred_grade = [], []
        for funny, grade in zip(labels_test_funny, labels_test_grade):
            pred_funny.append((random.choice([True, False]), funny))
            pred_grade.append((numpy.random.randint(0, 10), grade))
        str0 += "\n".join(["", tested_usr, ms.all_mesure_funny(pred_funny),
                           ms.all_mesure_grade(pred_grade)])
        all_usr_funny.extend(pred_funny)
        all_usr_grade.extend(pred_grade)
    str0 += "\n".join(["", "all_usr", ms.all_mesure_funny(all_usr_funny),
                       ms.all_mesure_grade(all_usr_grade)])
    print(str0)


if __name__ == '__main__':
    main()
