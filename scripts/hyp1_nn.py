#!/usr/bin/env python3
import utils.datasets as ds
import machine_learning.neural_network as nn
from collections import defaultdict as dd
import utils.mesure as ms
import json


def get_corpus():
    usr_vid, vid_usr, lusr, lvid = ds.combine_datas()
    hyp1 = ds.by_X(usr_vid)
    corpus = {}
    for usr in sorted(hyp1):
        list_uv = hyp1[usr]["keys"]
        vecs_test = ds.list_features(
            hyp1, [usr], "test", lvid, "vec")
        labels_test_funny = ds.list_features(
            hyp1, [usr], "test", lvid, "funny")
        vecs_train = ds.list_features(
            hyp1, [usr], "train", list_uv, "vec")
        labels_train_funny = ds.list_features(
            hyp1, [usr], "train", list_uv, "funny")
        corpus[usr] = [vecs_train, vecs_test,
                       labels_test_funny, labels_train_funny]
    return corpus


def train_model(corpus):
    str0 = ""
    sum_by_epochs = dd(list)
    loss_acc_by_epochs_test = dd(lambda: dd(list))
    loss_acc_by_epochs_train = dd(lambda: dd(list))
    for usr in sorted(corpus):
        vecs_train, vecs_test = corpus[usr][:2]
        labels_test_funny, labels_train_funny = corpus[usr][2:]
        model = nn.create_trained_nn(vecs_train, labels_train_funny, 1)
        for epochs in range(1, 151):
            pred_funny = nn.predict_nn(model, vecs_test, labels_test_funny)
            str0 += "\nEpochs: {}\n".format(epochs - 1)
            str0 += "\n".join(["", usr,
                               ms.all_mesure_funny(pred_funny)])
            model = nn.retrain_model(
                model, vecs_train, labels_train_funny, 1)
            sum_by_epochs[epochs].extend(pred_funny)
            loss_acc_by_epochs_test[usr][epochs].extend(  # tuple(loss, acc)
                tuple(model.evaluate(vecs_test, labels_test_funny)))
            loss_acc_by_epochs_train[usr][epochs].extend(  # tuple(loss, acc)
                tuple(model.evaluate(vecs_train, labels_train_funny)))
    for epochs in sum_by_epochs:
        str0 += "\nEpochs: {}\n".format(epochs)
        str0 += "\n".join(["", "all_usr",
                           ms.all_mesure_funny(sum_by_epochs[epochs])])
    return loss_acc_by_epochs_test, loss_acc_by_epochs_train, str0


def main():
    corpus = get_corpus()
    loss_acc_by_epochs_test, loss_acc_by_epochs_train, str0 = train_model(
        corpus)
    with open("../test_trained_nn/hyp1.txt", "w") as stream:
        stream.write(str0)
    with open("../test_trained_nn/loss_acc_hyp1.json", "w") as stream:
        json.dump(loss_acc_by_epochs_test, stream)
    with open("../test_trained_nn/loss_acc_hyp1_train.json", "w") as stream:
        json.dump(loss_acc_by_epochs_train, stream)


if __name__ == '__main__':
    main()
