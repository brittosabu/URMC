import pandas as pd
from itertools import combinations
import seaborn as sns
import matplotlib.pyplot as plt

class URMC:

    def __init__(self,features):
        """
        Initializing weights and features
        """
        self.feature_columns = features
        self.weights = {col: 0 for col in self.feature_columns}

    def fit(self,data):
        """
        Function to calculate weights using URMC
        ----------------------------------------
        Input:
         data : Data on which weights needs to be calculated
        Output:
         None
        """

        for pair in combinations(self.feature_columns,2):
            
            r = data[pair[0]].corr(data[pair[1]])

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

    def visalize_features(self):
        """
        Function to Visualize the weights and features
        """
        sns.swarmplot(x=list(self.weights.values()),y=list(self.weights.keys()),size=9)
        plt.show()

    def score(self,data):
        """
        Function to score based on trained weights
        ------------------------------------------
        Input:
         data : Data to be score
        Output:
         score : Scored data as a series
        """
        data['score'] = 0 
        for col,weight in self.weights.items():
            data['score']+= data[col]*weight

        return data['score']


