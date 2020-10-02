import argparse


class NegateAction(argparse.Action):
    def __call__(self, parser, ns, values, option):
        setattr(ns, self.dest, option[2:4] != "no")


def dict_to_querystring(params):
    qs = []
    for key in params:
        qs.append(f"{key}={params[key]}")
    return "&".join(qs)
