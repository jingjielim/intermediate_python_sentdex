import multiprocessing

def spawn(num):
    print('Spawned! {}'.format(num))

if __name__ == '__main__':
    for i in range(550):
        p = multiprocessing.Process(target=spawn, args=(i,))
        # if there isn't a need to wait for processes then just use p.start
        p.start()
        # join is used when u want to spawn and wait for processes to complete
        # p.join()
