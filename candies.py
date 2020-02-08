'''source :
https://www.hackerrank.com/challenges/candies/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming
https://www.youtube.com/watch?v=h6_lIwZYHQw
'''

ratings =[12,4,3,11,34,34,1,67]
ratings=[1,2,2]

    candies_ltr= [1] * len(ratings)

    candies_rtl= [1] * len(ratings)

        
    for i in range(0,len(ratings)-1):
        if ratings[i] > ratings[i+1] :
            if candies_ltr[i] < candies_ltr[i+1] or candies_ltr[i] ==1:
                candies_ltr[i] = candies_ltr[i+1] + 1 
        elif ratings[i] < ratings[i+1]:
            if candies_ltr[i+1] < candies_ltr[i] or candies_ltr[i+1]==1:
                candies_ltr[i+1] = candies_ltr[i] + 1
        else:
            continue

    for i in range(len(ratings)-1,0,-1):
       
        if ratings[i] > ratings[i-1] :
            if candies_rtl[i] < candies_rtl[i-1] or candies_rtl[i] ==1:
                candies_rtl[i] = candies_rtl[i-1] + 1 
        elif ratings[i] < ratings[i-1]:
            if candies_rtl[i-1] < candies_rtl[i] or candies_rtl[i-1] ==1:
                candies_rtl[i-1] = candies_rtl[i] + 1
        else:
            continue
        
    candies = [max(i,j) for i,j in zip(candies_ltr,candies_rtl)]

    return sum(candies)