# “ab”是地址（Address）簿（Book）的缩写

ab = {
    # 字典的键需要可计算散列值
    'Swaroop': ["swaroop@mozilla.org"], # 字典的值可以是任何对象
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is", ab['Swaroop'])

print('matz@ruby-lang.org' in ab.values())
print("Spammer" in ab.keys())

# 删除一对键值—值配对
ab.pop('Spammer')

print(f'\nThere are {len(ab)} contacts in the address-book\n')

for name, address in ab.items():
    print(f'Contact {name} at {address}')
for contactor in ab.keys():
    print(f'Found contactor {contactor}')
for address in ab.values():
    print(f'Found address {address}')

# 添加一对键值—值配对
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab: # 注意 in 检查默认是对 keys() 判断
    print("\nGuido's address is", ab['Guido'])
