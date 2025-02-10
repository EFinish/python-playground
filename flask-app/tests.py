from potatoservice import PotatoService

def run_tests():
    johnPotato1 = "just #chilling today"
    johnPotato2 = "eating #steak for dinner"
    johnPotato3 = "ugh! this #steak tasted like dog food"

    service = PotatoService()

    service.add_user("john")
    if not service.user_exists("john"):
        print("add_user failed to add john, or user_exists failed to find john")

    service.add_post("john", johnPotato1, 1)
    service.add_post("john", johnPotato2, 2)
    service.add_post("john", johnPotato3, 3)

    johnPosts = service.get_posts_for_user("john")

    if len(johnPosts) != 3:
        print("expected 3 posts for john, got", len(johnPosts))
    if not johnPotato1 in johnPosts:
        print("expected ", johnPotato1," in John's posts but did not find it")
    if not johnPotato2 in johnPosts:
        print("expected ", johnPotato2," in John's posts but did not find it")
    if not johnPotato3 in johnPosts:
        print("expected ", johnPotato3," in John's posts but did not find it")

    steakPosts = service.get_posts_for_topic("steak")

    if len(steakPosts) != 2:
        print("expected 2 posts for steak, got", len(steakPosts))
    if not johnPotato2 in steakPosts:
        print("expected ", johnPotato2," in steak posts but did not find it")
    if not johnPotato3 in steakPosts:
        print("expected ", johnPotato3," in steak posts but did not find it")
    
    trendingTopicsLonger = service.get_trending_topics(1, 3)

    if "steak" not in trendingTopicsLonger:
        print("expected steak in longer-term trending topics, but did not find it")
    if "chilling" not in trendingTopicsLonger:
        print("expected chilling in longer-term trending topics, but did not find it")
    if not trendingTopicsLonger[0] == "steak":
        print("expected steak to be the top trending topic, but got", trendingTopicsLonger[0])
    if not trendingTopicsLonger[1] == "chilling":
        print("expected chilling to be the second trending topic, but got", trendingTopicsLonger[1])

    print("Tests complete. If nothing else printed, all tests passed.")

run_tests()