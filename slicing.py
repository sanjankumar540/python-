'''s = "pythonProgramming"
print(s[0:6:])

print(s[6::])

print(s[2:6:1])

print(s[9:13:])

print(s[6:13:1])

print(s[-4::1])

print(s[6:9:])

print(s[11:14:])

print(s[4:9])

print(s[3:9])

print(s[1:4])

print(s[10:13])

print(s[14::])

print(s[0:4])

print(s[9:13])

print(s[0:9])

print(s[16:5:-1])

print(s[5::-1])

print(s[12:8:-1])

print(s[5:1:-1])

print('-'*60)

t = "ArtificialIntelligence"
print(t[-22:-12:1])

print(t[-12::1])

print(t[-18:-12:1])

print(t[-12:-7:1])

print(t[-5::1])

print(t[-20:-15:1])

print(t[-16:-10:1])
print(t[-9::1])
print(t[-13:-23:-1])
print(t[-1:-13:-1])
print(t[-8:-13:-1])
print(t[-1:-6:-1])
print(t[-16:-12:1])
print(t[-8:-4:1])
print(t[-10::1])

print('-'*60)

word = "computerscience"

print(word[::2])
print(word[1::2])
x = word[-1:-3:-1]
y = word[-4:-7:-1]
print(x+y)
print(word[-1:-8:-1])
print(word[-2:-4:-1]+word[-7])
print(word[-4:-7:-1])
print(word[0:5:2])
print(word[-1]+word[-3:-5:-1]+word[-6])
print(word[8::2])
print(word[-1::-2])

print('-'*60)

nums = [1,2,3,4,5,6,7,8,9,10,11,12]
print(nums[0::2])
print(nums[-11::2])
print(nums[-1:-6:-1])
print(nums[-1::-2])
print(nums[-8:-4])
print(nums[-5:-9:-1])
print(nums[2::3])
print(nums[-2:-20:-3])
print(nums[0:10:3])
print(nums[-3:-20:-3])

print('-'*60)
 
items = [["apple","banana","cherry","mango"],
         [100,200,300,400,500],
         "programming",
         ["red","green","blue","yellow"],
         [1,2,3,4,5,6],
         "artificial"]
print(items[-6][-4:-2:1])
print(items[-6][-2::1])
print(items[-5][-4:-1:1])
print(items[-5][-3::1])
print(items[-4][-12:-4:1])
print(items[-4][-1:-12:-1])
print(items[-4][-10:-1:2])
print(items[-3][-3:-1:1])
print(items[-3][-1:-4:-1])
print(items[-2][-5::2])'''




arr =[
10, 20, 30, 40, 'python', 'Roses are red', [1, 2, 3, 4, 5 ] ,
['apple', 'banana', 'cherry', ['x', 'y', 'z'] ],
(100, 200 , 300, (400, 500, ('deep', 'nest'))) , {10, 20, 30}, 3.1415,
['list', ['nested', ['deeply', ['super deep']]]], 'abcdefghi',
['mix', 123, 4.56, (7, 8, 9)], [[[ 'A', 'B'], 'C' ], 'D'], 'END', ('language',),
('python',)
]

# executing using forward slicing
print(arr[0:4:1])
print(arr[1:4:1])
print(arr[4][::])
print(arr[5][::])
print(arr[5][6:9:1])
print(arr[6][0:3:])
print(arr[6][3:6:1])
print(arr[5])
print(arr[7][0:2])
print(arr[7][1][::])
print(arr[7][2][::])
print(arr[7][3][0:2:1])
print(arr[7][3][1])
print(arr[7][3][2])
print(arr[8][0:2:1])
print(arr[8][2])
print(arr[8][3][0:2:1])
print(arr[-1][0][::-1])
print(arr[7][3][0:3:2])
print(arr[-4][0][0])
print(arr[-3][2] + arr[-3][0:2])
print(arr[-2][0][::-1])
print(arr[-1][0][::])
print(arr[11][1][1][1][::])
print(arr[11][1][0][0:6])

print ('_'*100)
arr =[
10, 20, 30, 40, 'python', 'Roses are red', [1, 2, 3, 4, 5 ] ,
['apple', 'banana', 'cherry', ['x', 'y', 'z'] ],
(100, 200 , 300, (400, 500, ('deep', 'nest'))) , {10, 20, 30}, 3.1415,
['list', ['nested', ['deeply', ['super deep']]]], 'abcdefghi',
['mix', 123, 4.56, (7, 8, 9)], [[[ 'A', 'B'], 'C' ], 'D'], 'END', ('language',),
('python',)
]

# executing the same using backward sclicing
print(arr[-18:-14:1]) #[10, 20, 30, 40]
print(arr[-17:-14:1])#[20, 30, 40]
print(arr[-14][::1])#python
print(arr[-13][::1])#Roses are red
print(arr[-13][-13:-8:1])#Roses
print(arr[-13][-7:-4:1])#are
print(arr[-12][-5:-2:1])#[1, 2, 3]
print(arr[-12][-2::1])#[4, 5]
print(arr[-11][-4:-2:1])#['apple', 'banana']
print(arr[-11][-3])#banana
print(arr[-11][-2][-6::1])#cherry
print(arr[-11][-1][-3:-1:1]) #['x', 'y']
print(arr[-11][-1][-2][::]) #y
print(arr[-11][-1][-1][::]) #z
print(arr[-10][-4:-2:1]) #(100, 200)
print(arr[-10][-2]) #300
print(arr[-10][-1][-3:-1:1]) #(400, 500)
print(arr[-1][-1][::-1]) #nohtyp
print(arr[-11][-1][-3::2]) #['x', 'z']
print(arr[-4][-2][-2][::]) #['A', 'B']
print(arr[-3][-1]+arr[-3][-3:-1:1]) #DEN
print(arr[-2][-1][::-1]) #egaugnal
print(arr[-14][::-1]) #nohtyp
print(arr[-7][-1][-1][-1][::1]) #['super deep']
print(arr[-7][-1][-2][::1]) #nested
      

























