import tiles3 as tc


def main():
    iht = tc.IHT(1024)
    indices = tc.tiles(iht, 8, [3.6, 7.21])
    print indices
    indices = tc.tiles(iht, 8, [3.7, 7.21])
    print indices
    indices = tc.tiles(iht, 8, [4, 7])
    print indices
    indices = tc.tiles(iht, 8, [-37.2, 7])
    print indices

if __name__ == '__main__':
    main()
