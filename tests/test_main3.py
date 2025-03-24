import pytest
from main3 import Parrot

Parrot_1_who_dosent_like_me_for_no_reason = Parrot()

def test_parrot_talks():
    Parrot_1_who_dosent_like_me_for_no_reason = Parrot()
    assert Parrot_1_who_dosent_like_me_for_no_reason.talks == True

def test_parrot_hits_on_head():
    Parrot_1_who_dosent_like_me_for_no_reason = Parrot()
    assert Parrot_1_who_dosent_like_me_for_no_reason.hits_on_my_damn_head == True
    
result = pytest.main()
if result == 0:
    print("All tests passed! Parrot Typing is proved and is successful! ✅")
else:
    print(f"Tests failed with code: {result}. Parrot Typing Failed ❌")