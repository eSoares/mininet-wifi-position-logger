import time 

class LogNodePosition(threading.Thread):
    def __init__(self, node, outfile, tickrate = 1):
        self.node = node
        self.outfile = outfile
        self.tickrate = tickrate
        self.stop_ = False
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        start_time = time.time()
        with open(self.outfile, "w+") as out:
            while not self.stop_:
                if "position" in self.node.params:
                        out.write("%s, %s, %s" % self.node.params["position"])
                        out.write("%.0f" % (time.time()-start_time))
                time.sleep(self.tickrate)

    def stop(self):
        self.stop_ = True
