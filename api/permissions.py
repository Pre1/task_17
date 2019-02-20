from rest_framework.permissions import BasePermission


class IsOwnerOrStaff(BasePermission):
	message = "You must be either the Owner for the restaurant or Staff."

	def has_object_permission(self, request, view, obj):
		return request.user.is_staff or (obj.owner == request.user)

		