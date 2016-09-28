from django.core.exceptions import PermissionDenied
from permission.logics import PermissionLogic
from permission.utils.field_lookup import field_lookup
import logging
from logging import debug
logging.basicConfig(filename='/home/lnl/perms.log', level=logging.DEBUG)

class AssocUsersCustomPermissionLogic(PermissionLogic):
    field_name = 'authorized_users'
    perms = []
    denied = []

    def has_perm(self, user_obj, perm, obj=None):
        # User must be logged in
        if not user_obj.is_authenticated():
            debug("%s not signed in" % user_obj)
            return False
        # See if we can handle that perm
        if perm not in self.perms and perm not in self.denied:
            debug("permission %s not recognized" % perm)
            return False
        # if there isn't an object, that means we're looking for a module permission.
        # We don't do that.
        if obj is None:
            return False
        # If your account has been disabled, too bad.
        if not user_obj.is_active:
            debug("%s is not an active user" % user_obj)
            return False
        # get all authorized_users in the object
        if not hasattr(self.field_name, '__iter__'):
            self.field_name = [self.field_name]
        for lookup in self.field_name:
            authorized_users = field_lookup(obj, lookup)
            # break out of a generator expression
            if hasattr(authorized_users, 'next'):
                authorized_users = list(authorized_users)
            else:
                authorized_users = [authorized_users]
            for user in authorized_users:
                if hasattr(user, 'all'):
                    authorized_users.extend(user.all())
                    authorized_users.remove(user)
            if (user_obj in authorized_users):
                if perm in self.denied:
                    debug("%s denied for %s in lookup '%s'" % (perm, user_obj, lookup))
                    raise PermissionDenied()
                return True


class CrewChiefPermLogic(AssocUsersCustomPermissionLogic):
    field_name = 'ccinstances__crew_chief'
    perms = ('events.view_event', 'events.event_images', 'events.cancel_event',
             'events.event_attachments', 'events.edit_event_times',
             'events.add_event_report', 'events.edit_event_text',
             'events.view_hidden_event', 'events.edit_event_fund',
             'events.view_event_billing', 'events.adjust_event_charges',
             'events.event_view_sensitive')


class EventContactPermLogic(AssocUsersCustomPermissionLogic):
    field_name = 'contact'
    perms = ('events.view_event', 'events.event_images', 'events.cancel_event',
             'events.event_attachments', 'events.edit_event_times',
             'events.add_event_report', 'events.edit_event_text',
             'events.view_hidden_event', 'events.edit_event_fund',
             'events.view_event_billing')


class EventCreatorPermLogic(AssocUsersCustomPermissionLogic):
    field_name = 'submitted_by'
    perms = ('events.view_event', 'events.event_images', 'events.cancel_event',
             'events.event_attachments', 'events.edit_event_times',
             'events.add_event_report', 'events.edit_event_text',
             'events.view_hidden_event', 'events.edit_event_fund',
             'events.view_event_billing', 'events.edit_event_flags',
             'events.view_test_event')


class EventOrgMemberPermLogic(AssocUsersCustomPermissionLogic):
    field_name = 'org__associated_users'
    perms = ('events.view_event', 'events.event_images', 'events.cancel_event',
             'events.event_attachments', 'events.edit_event_times',
             'events.add_event_report', 'events.edit_event_text',
             'events.view_hidden_event', 'events.edit_event_fund',
             'events.view_event_billing')


class EventOrgOwnerPermLogic(AssocUsersCustomPermissionLogic):
    field_name = 'org__user_in_charge'
    perms = EventOrgMemberPermLogic.perms + \
        ('events.edit_event_flags', 'events.adjust_event_owner')


class WorkedAtEventPermLogic(AssocUsersCustomPermissionLogic):
    field_name = 'hours__user'
    perms = ('events.view_event', 'events.add_event_report', 'events.event_images')


class OrgMemberPermLogic(AssocUsersCustomPermissionLogic):
    field_name = 'associated_users'
    perms = ('events.view_org', 'events.list_org_events', 'events.list_org_members', 'events.create_org_event',
             'events.show_org_billing')


class OrgOwnerPermLogic(AssocUsersCustomPermissionLogic):
    field_name = 'user_in_charge'
    perms = OrgMemberPermLogic.perms + ('events.edit_org', 'events.edit_org_billing', 'events.edit_org_members',
                                        'events.transfer_org_ownership', 'events.deprecate_org',
                                        'events.list_org_hidden_events')

class ReportAuthorPermLogic(AssocUsersCustomPermissionLogic):
    field_name = 'crew_chief'
    perms = ('events.delete_ccreport', 'events.change_ccreport')

PERMISSION_LOGICS = (
    ('events.Event', CrewChiefPermLogic()),
    ('events.Event', EventContactPermLogic()),
    ('events.Event', EventCreatorPermLogic()),
    ('events.Event', WorkedAtEventPermLogic()),
    ('events.Event', EventOrgMemberPermLogic()),
    ('events.Event', EventOrgOwnerPermLogic()),
    ('events.Organization', OrgMemberPermLogic()),
    ('events.Organization', OrgOwnerPermLogic()),
    ('events.CCReport', ReportAuthorPermLogic()),
)
