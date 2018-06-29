#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Module with temperature scale conversion
"""
import argparse


def fahr_to_kelv(temperature):
    """
    Takes a temperature `temp` in fahrenheit and returns it in Kelvin
    """
    kelvin = 5./9. * (temperature - 32.) + 273.15
    return kelvin


def fahr_to_cels(temperature):
    """
    Takes a temperature `temp` in kelvin and returns it in celsius
    """
    kelvin = fahr_to_kelv(temperature)
    celsius = kelvin - 273.15
    return celsius


def main():
    """
    For entry point
    """
    parser = argparse.ArgumentParser("Convert temperature in fahrenheit to kelvin or celsius")
    parser.add_argument("temperature", help="Temperature in fahrenheit")
    parser.add_argument("-c", "--celsius", action="store_true", help="Convert to celsius scale")

    args = parser.parse_args()

    f = args.temperature

    if args.is_celsius:
        c = fahr_to_cels(f)
        print("Temperature %5.3f fahrenheit equals %5.3f celsius" % (f, c))
    else:
        k = fahr_to_kelv(f)
        print("Temperature %5.3f fahrenheit equals %5.3f kelvin" % (f, k))

