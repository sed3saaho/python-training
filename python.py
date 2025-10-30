favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil' : 'python',
}
friends = ['phil', 'sarah']
for name in favorite_language.keys():
    print(name.title())
    
    if name in friends:
        language = favorite_language[name].title()
        print(f"/t{name.title()}, I see you love{language}")
    
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil' : 'python',
}
if 'erin' not in favorite_language.key():
    print("Erin, please take our poll!")