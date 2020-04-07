# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class Severity(str, Enum):

    sev0 = "Sev0"
    sev1 = "Sev1"
    sev2 = "Sev2"
    sev3 = "Sev3"
    sev4 = "Sev4"


class SignalType(str, Enum):

    metric = "Metric"
    log = "Log"
    unknown = "Unknown"


class AlertState(str, Enum):

    new = "New"
    acknowledged = "Acknowledged"
    closed = "Closed"


class MonitorCondition(str, Enum):

    fired = "Fired"
    resolved = "Resolved"


class MonitorService(str, Enum):

    application_insights = "Application Insights"
    activity_log_administrative = "ActivityLog Administrative"
    activity_log_security = "ActivityLog Security"
    activity_log_recommendation = "ActivityLog Recommendation"
    activity_log_policy = "ActivityLog Policy"
    activity_log_autoscale = "ActivityLog Autoscale"
    log_analytics = "Log Analytics"
    nagios = "Nagios"
    platform = "Platform"
    scom = "SCOM"
    service_health = "ServiceHealth"
    smart_detector = "SmartDetector"
    vm_insights = "VM Insights"
    zabbix = "Zabbix"


class AlertModificationEvent(str, Enum):

    alert_created = "AlertCreated"
    state_change = "StateChange"
    monitor_condition_change = "MonitorConditionChange"


class SmartGroupModificationEvent(str, Enum):

    smart_group_created = "SmartGroupCreated"
    state_change = "StateChange"
    alert_added = "AlertAdded"
    alert_removed = "AlertRemoved"


class State(str, Enum):

    new = "New"
    acknowledged = "Acknowledged"
    closed = "Closed"


class ScopeType(str, Enum):

    resource_group = "ResourceGroup"
    resource = "Resource"


class Operator(str, Enum):

    equals = "Equals"
    not_equals = "NotEquals"
    contains = "Contains"
    does_not_contain = "DoesNotContain"


class SuppressionType(str, Enum):

    always = "Always"
    once = "Once"
    daily = "Daily"
    weekly = "Weekly"
    monthly = "Monthly"


class ActionRuleStatus(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class AlertRuleState(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class TimeRange(str, Enum):

    oneh = "1h"
    oned = "1d"
    sevend = "7d"
    three_zerod = "30d"


class AlertsSortByFields(str, Enum):

    name = "name"
    severity = "severity"
    alert_state = "alertState"
    monitor_condition = "monitorCondition"
    target_resource = "targetResource"
    target_resource_name = "targetResourceName"
    target_resource_group = "targetResourceGroup"
    target_resource_type = "targetResourceType"
    start_date_time = "startDateTime"
    last_modified_date_time = "lastModifiedDateTime"


class AlertsSummaryGroupByFields(str, Enum):

    severity = "severity"
    alert_state = "alertState"
    monitor_condition = "monitorCondition"
    monitor_service = "monitorService"
    signal_type = "signalType"
    alert_rule = "alertRule"


class SmartGroupsSortByFields(str, Enum):

    alerts_count = "alertsCount"
    state = "state"
    severity = "severity"
    start_date_time = "startDateTime"
    last_modified_date_time = "lastModifiedDateTime"
