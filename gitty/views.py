from django.http import JsonResponse
import requests

def member_list(request):
	bob = request.user

	social_account = bob.socialaccount_set.get(user=bob.id)
	social_token = social_account.socialtoken_set.get(account=social_account.id)
	token = social_token.token

	# url = "https://api.github.com/orgs/joinCODED/members"
	url = "https://api.github.com/users/fsalsayegh/repos"
	res = requests.get(url, headers={"Authorization": "token "+token})
	return JsonResponse(res.json(), safe=False)