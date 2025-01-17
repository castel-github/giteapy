# coding: utf-8

# flake8: noqa
"""
    Gitea API

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.23.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from giteapy.models.api_error import APIError
from giteapy.models.access_token import AccessToken
from giteapy.models.action_task import ActionTask
from giteapy.models.action_task_response import ActionTaskResponse
from giteapy.models.action_variable import ActionVariable
from giteapy.models.activity import Activity
from giteapy.models.activity_pub import ActivityPub
from giteapy.models.add_collaborator_option import AddCollaboratorOption
from giteapy.models.add_time_option import AddTimeOption
from giteapy.models.annotated_tag import AnnotatedTag
from giteapy.models.annotated_tag_object import AnnotatedTagObject
from giteapy.models.attachment import Attachment
from giteapy.models.badge import Badge
from giteapy.models.branch import Branch
from giteapy.models.branch_protection import BranchProtection
from giteapy.models.change_file_operation import ChangeFileOperation
from giteapy.models.change_files_options import ChangeFilesOptions
from giteapy.models.changed_file import ChangedFile
from giteapy.models.combined_status import CombinedStatus
from giteapy.models.comment import Comment
from giteapy.models.commit import Commit
from giteapy.models.commit_affected_files import CommitAffectedFiles
from giteapy.models.commit_date_options import CommitDateOptions
from giteapy.models.commit_meta import CommitMeta
from giteapy.models.commit_stats import CommitStats
from giteapy.models.commit_status import CommitStatus
from giteapy.models.commit_status_state import CommitStatusState
from giteapy.models.commit_user import CommitUser
from giteapy.models.compare import Compare
from giteapy.models.contents_response import ContentsResponse
from giteapy.models.create_access_token_option import CreateAccessTokenOption
from giteapy.models.create_branch_protection_option import CreateBranchProtectionOption
from giteapy.models.create_branch_repo_option import CreateBranchRepoOption
from giteapy.models.create_email_option import CreateEmailOption
from giteapy.models.create_file_options import CreateFileOptions
from giteapy.models.create_fork_option import CreateForkOption
from giteapy.models.create_gpg_key_option import CreateGPGKeyOption
from giteapy.models.create_hook_option import CreateHookOption
from giteapy.models.create_hook_option_config import CreateHookOptionConfig
from giteapy.models.create_issue_comment_option import CreateIssueCommentOption
from giteapy.models.create_issue_option import CreateIssueOption
from giteapy.models.create_key_option import CreateKeyOption
from giteapy.models.create_label_option import CreateLabelOption
from giteapy.models.create_milestone_option import CreateMilestoneOption
from giteapy.models.create_o_auth2_application_options import CreateOAuth2ApplicationOptions
from giteapy.models.create_or_update_secret_option import CreateOrUpdateSecretOption
from giteapy.models.create_org_option import CreateOrgOption
from giteapy.models.create_pull_request_option import CreatePullRequestOption
from giteapy.models.create_pull_review_comment import CreatePullReviewComment
from giteapy.models.create_pull_review_options import CreatePullReviewOptions
from giteapy.models.create_push_mirror_option import CreatePushMirrorOption
from giteapy.models.create_release_option import CreateReleaseOption
from giteapy.models.create_repo_option import CreateRepoOption
from giteapy.models.create_status_option import CreateStatusOption
from giteapy.models.create_tag_option import CreateTagOption
from giteapy.models.create_tag_protection_option import CreateTagProtectionOption
from giteapy.models.create_team_option import CreateTeamOption
from giteapy.models.create_user_option import CreateUserOption
from giteapy.models.create_variable_option import CreateVariableOption
from giteapy.models.create_wiki_page_options import CreateWikiPageOptions
from giteapy.models.cron import Cron
from giteapy.models.delete_email_option import DeleteEmailOption
from giteapy.models.delete_file_options import DeleteFileOptions
from giteapy.models.deploy_key import DeployKey
from giteapy.models.dismiss_pull_review_options import DismissPullReviewOptions
from giteapy.models.edit_attachment_options import EditAttachmentOptions
from giteapy.models.edit_branch_protection_option import EditBranchProtectionOption
from giteapy.models.edit_deadline_option import EditDeadlineOption
from giteapy.models.edit_git_hook_option import EditGitHookOption
from giteapy.models.edit_hook_option import EditHookOption
from giteapy.models.edit_issue_comment_option import EditIssueCommentOption
from giteapy.models.edit_issue_option import EditIssueOption
from giteapy.models.edit_label_option import EditLabelOption
from giteapy.models.edit_milestone_option import EditMilestoneOption
from giteapy.models.edit_org_option import EditOrgOption
from giteapy.models.edit_pull_request_option import EditPullRequestOption
from giteapy.models.edit_reaction_option import EditReactionOption
from giteapy.models.edit_release_option import EditReleaseOption
from giteapy.models.edit_repo_option import EditRepoOption
from giteapy.models.edit_tag_protection_option import EditTagProtectionOption
from giteapy.models.edit_team_option import EditTeamOption
from giteapy.models.edit_user_option import EditUserOption
from giteapy.models.email import Email
from giteapy.models.external_tracker import ExternalTracker
from giteapy.models.external_wiki import ExternalWiki
from giteapy.models.file_commit_response import FileCommitResponse
from giteapy.models.file_delete_response import FileDeleteResponse
from giteapy.models.file_links_response import FileLinksResponse
from giteapy.models.file_response import FileResponse
from giteapy.models.files_response import FilesResponse
from giteapy.models.gpg_key import GPGKey
from giteapy.models.gpg_key_email import GPGKeyEmail
from giteapy.models.general_api_settings import GeneralAPISettings
from giteapy.models.general_attachment_settings import GeneralAttachmentSettings
from giteapy.models.general_repo_settings import GeneralRepoSettings
from giteapy.models.general_ui_settings import GeneralUISettings
from giteapy.models.generate_repo_option import GenerateRepoOption
from giteapy.models.git_blob_response import GitBlobResponse
from giteapy.models.git_entry import GitEntry
from giteapy.models.git_hook import GitHook
from giteapy.models.git_object import GitObject
from giteapy.models.git_tree_response import GitTreeResponse
from giteapy.models.gitignore_template_info import GitignoreTemplateInfo
from giteapy.models.hook import Hook
from giteapy.models.identity import Identity
from giteapy.models.inline_response200 import InlineResponse200
from giteapy.models.inline_response2001 import InlineResponse2001
from giteapy.models.internal_tracker import InternalTracker
from giteapy.models.issue import Issue
from giteapy.models.issue_config import IssueConfig
from giteapy.models.issue_config_contact_link import IssueConfigContactLink
from giteapy.models.issue_config_validation import IssueConfigValidation
from giteapy.models.issue_deadline import IssueDeadline
from giteapy.models.issue_form_field import IssueFormField
from giteapy.models.issue_form_field_type import IssueFormFieldType
from giteapy.models.issue_form_field_visible import IssueFormFieldVisible
from giteapy.models.issue_labels_option import IssueLabelsOption
from giteapy.models.issue_meta import IssueMeta
from giteapy.models.issue_template import IssueTemplate
from giteapy.models.issue_template_string_slice import IssueTemplateStringSlice
from giteapy.models.label import Label
from giteapy.models.label_template import LabelTemplate
from giteapy.models.license_template_info import LicenseTemplateInfo
from giteapy.models.licenses_template_list_entry import LicensesTemplateListEntry
from giteapy.models.markdown_option import MarkdownOption
from giteapy.models.markup_option import MarkupOption
from giteapy.models.merge_pull_request_option import MergePullRequestOption
from giteapy.models.merge_upstream_request import MergeUpstreamRequest
from giteapy.models.merge_upstream_response import MergeUpstreamResponse
from giteapy.models.migrate_repo_options import MigrateRepoOptions
from giteapy.models.milestone import Milestone
from giteapy.models.new_issue_pins_allowed import NewIssuePinsAllowed
from giteapy.models.node_info import NodeInfo
from giteapy.models.node_info_services import NodeInfoServices
from giteapy.models.node_info_software import NodeInfoSoftware
from giteapy.models.node_info_usage import NodeInfoUsage
from giteapy.models.node_info_usage_users import NodeInfoUsageUsers
from giteapy.models.note import Note
from giteapy.models.notification_count import NotificationCount
from giteapy.models.notification_subject import NotificationSubject
from giteapy.models.notification_thread import NotificationThread
from giteapy.models.notify_subject_type import NotifySubjectType
from giteapy.models.o_auth2_application import OAuth2Application
from giteapy.models.organization import Organization
from giteapy.models.organization_permissions import OrganizationPermissions
from giteapy.models.pr_branch_info import PRBranchInfo
from giteapy.models.package import Package
from giteapy.models.package_file import PackageFile
from giteapy.models.payload_commit import PayloadCommit
from giteapy.models.payload_commit_verification import PayloadCommitVerification
from giteapy.models.payload_user import PayloadUser
from giteapy.models.permission import Permission
from giteapy.models.public_key import PublicKey
from giteapy.models.pull_request import PullRequest
from giteapy.models.pull_request_meta import PullRequestMeta
from giteapy.models.pull_review import PullReview
from giteapy.models.pull_review_comment import PullReviewComment
from giteapy.models.pull_review_request_options import PullReviewRequestOptions
from giteapy.models.push_mirror import PushMirror
from giteapy.models.reaction import Reaction
from giteapy.models.reference import Reference
from giteapy.models.release import Release
from giteapy.models.rename_user_option import RenameUserOption
from giteapy.models.repo_collaborator_permission import RepoCollaboratorPermission
from giteapy.models.repo_commit import RepoCommit
from giteapy.models.repo_topic_options import RepoTopicOptions
from giteapy.models.repo_transfer import RepoTransfer
from giteapy.models.repository import Repository
from giteapy.models.repository_meta import RepositoryMeta
from giteapy.models.review_state_type import ReviewStateType
from giteapy.models.search_results import SearchResults
from giteapy.models.secret import Secret
from giteapy.models.server_version import ServerVersion
from giteapy.models.state_type import StateType
from giteapy.models.stop_watch import StopWatch
from giteapy.models.submit_pull_review_options import SubmitPullReviewOptions
from giteapy.models.tag import Tag
from giteapy.models.tag_protection import TagProtection
from giteapy.models.team import Team
from giteapy.models.time_stamp import TimeStamp
from giteapy.models.timeline_comment import TimelineComment
from giteapy.models.topic_name import TopicName
from giteapy.models.topic_response import TopicResponse
from giteapy.models.tracked_time import TrackedTime
from giteapy.models.transfer_repo_option import TransferRepoOption
from giteapy.models.update_branch_protection_priories import UpdateBranchProtectionPriories
from giteapy.models.update_branch_repo_option import UpdateBranchRepoOption
from giteapy.models.update_file_options import UpdateFileOptions
from giteapy.models.update_repo_avatar_option import UpdateRepoAvatarOption
from giteapy.models.update_user_avatar_option import UpdateUserAvatarOption
from giteapy.models.update_variable_option import UpdateVariableOption
from giteapy.models.user import User
from giteapy.models.user_badge_option import UserBadgeOption
from giteapy.models.user_heatmap_data import UserHeatmapData
from giteapy.models.user_settings import UserSettings
from giteapy.models.user_settings_options import UserSettingsOptions
from giteapy.models.watch_info import WatchInfo
from giteapy.models.wiki_commit import WikiCommit
from giteapy.models.wiki_commit_list import WikiCommitList
from giteapy.models.wiki_page import WikiPage
from giteapy.models.wiki_page_meta_data import WikiPageMetaData
