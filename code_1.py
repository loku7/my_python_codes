'''
Created on Nov 13, 2015

@author: LOKU
'''
    class Holes(object):
        def __init__(self):
            self.num_test = int(raw_input())
            self.inputs = []
            for i in range(0,self.num_test):
                self.inputs.append(raw_input())
            self.hole = {'A':1,
                    'B':2,
                    'D':1,
                    'O':1,
                    'P':1,
                    'Q':1,
                    'R':1}
            for inputs in self.inputs:
                print self.input_split(inputs)
        def input_split(self,inputs):
            sum  = 0
            for word in inputs:
                try:
                    sum +=self.hole[word]
                except KeyError:
                    pass
            return sum
     
    def main():
        holes = Holes()
     
     
    if __name__=="__main__":
        main() 