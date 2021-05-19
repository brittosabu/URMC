import pandas as pd
from itertools import combinations

class URMC:

    def __init__(self,features):
        """
        """
        self.feature_columns = features
        self.weights = {col: 0 for col in self.feature_columns}

    def calculate_weights(self,data):
        """
        
        """

        for pair in combinations(self.feature_cols,2):
            
            r = data[pair[0]].r(data[pair[1]])

            wi=self.weights[pair[0]]
            wj=self.weights[pair[1]]
            
            if r>=0:
                if wi>=0 and wj>=0:
                    wi=wi+r
                    wj=wj+r
                elif wi<0 and wj<0:
                    wi=wi-r
                    wj=wj-r
                elif wi>=0 and wj<0:
                    wi=wi-r
                    wj=wj+r
                else:
                    wi=wi+r
                    wj=wj-r
            else:
                if wi>=0 and wj>=0:
                    if wi<wj:
                        wi=wi+r
                        wj=wj-r
                    else:
                        wi=wi-r
                        wj=wj+r

                elif wi<0 and wj<0:
                    if wi<wj:
                        wi=wi+r
                        wj=wj-r
                    else:
                        wi=wi-r
                        wj=wj+r
                    wi=wi-r
                    wj=wj-r
                elif wi>=0 and wj<0:
                    wi=wi-r
                    wj=wj+r
                else:
                    wi=wi+r
                    wj=wj-r

            self.weights[pair[0]]=wi
            self.weights[pair[1]]=wj

        return self.weights

    def calculate_ranks(self,data):
        """
        """
        data['score'] = 0 
        for col,weight in self.weights:
            data['score']+= data[col]*weight

        return data['score']


