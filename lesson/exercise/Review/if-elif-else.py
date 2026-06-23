#     int a = 5;
#     if (a > 5){
#         printf("A");
#     }else if(a == 5){
#         a++;
#         if (a != 5){
#             printf("C");
#         }else{
#             if (2 + 3 == a){
#                 printf("D");
#             }else{
#                 printf("E");
#             }
#         }
#     }else{
#         printf("F");
#     }
a = 5
if a > 5: 
    print("A")
else:
    for i in range(1, 5, 2):
        if i == 4: 
            break
        print(i)
    
