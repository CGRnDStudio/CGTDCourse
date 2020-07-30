=============================
Deadline渲染农场事件插件开发
=============================

- Deadline Event Plugins
- OnJobStarted
- OnSlaveIdle

- 深入Deadline API
- docs.thinkboxsoftware.com

关联任务

Deadline自定义Event插件

- 路径：DeadlineRepository10\custom\events
- 掌握调试技巧
- RepositoryUtils
- OnJobStarted

View Job Reports

OnJobStarted.param

.. code-block:: python

    [State]
    Type=Enum
    Items=Global Enabled;Opt-In;Disabled
    Category=Options
    CategoryOrder=0
    CategoryIndex=0
    Label=State
    Default=Disabled
    Description=How this event plug-in should respond to events. If Global, all jobs and slaves will trigger the events for this plugin. If Opt-In, jobs and slaves can choose to trigger the events for this plugin. If Disabled, no events are triggered for this plugin.

OnJobStarted.py

.. code-block:: python

    ###############################################################
    # Imports
    ###############################################################
    import math
    from System import *

    from Deadline.Events import *
    from Deadline.Scripting import *


    ##################################################################################################
    # This is the function called by Deadline to get an instance of the Draft event listener.
    ##################################################################################################
    def GetDeadlineEventListener():
        return OverrideJobPriorityListener()


    def CleanupDeadlineEventListener(eventListener):
        eventListener.Cleanup()


    ###############################################################
    # The event listener class.
    ###############################################################
    class OverrideJobPriorityListener(DeadlineEventListener):
        def __init__(self):
            self.OnJobStartedCallback += self.OnJobStarted

        def Cleanup(self):
            del self.OnJobStartedCallback

        def OnJobStarted(self, job):

            # Exit this event plugin as soon as possible if not a Houdini job
            if job.JobPlugin != "Houdini":
                return

            job.Priority = 80

            RepositoryUtils.SaveJob(job)

            jobs = RepositoryUtils.GetJobsInState(["Active", "Pending"])
            slaveSettings = RepositoryUtils.GetSlaveSettingsList(True)
            slaves = [x for x in slaveSettings if x.SlaveEnabled]

            if jobs and slaves:
                userNum = len(set(x.UserName for x in jobs if x.JobTaskCount != 2))

                self.LogInfo("User Num: %d" % userNum)
                self.LogInfo("Machine Num: %d" % len(slaves))

                if not userNum:
                    return

                num = int(math.ceil(float(len(slaves)) / float(userNum)))

                if userNum == 1:

                    for x in jobs:

                        if x.MachineLimit != 0:
                            self.LogInfo(x.Name)
                            RepositoryUtils.SetMachineLimitMaximum(x.ID, 0)

                else:

                    for x in jobs:

                        if x.MachineLimit != num:
                            self.LogInfo(x.Name)
                            RepositoryUtils.SetMachineLimitMaximum(x.ID, num)


- OnSlaveIdle

OnSlaveIdle.param

.. code-block:: python

    [State]
    Type=Enum
    Items=Global Enabled;Opt-In;Disabled
    Category=Options
    CategoryOrder=0
    CategoryIndex=0
    Label=State
    Default=Disabled
    Description=How this event plug-in should respond to events. If Global, all jobs and slaves will trigger the events for this plugin. If Opt-In, jobs and slaves can choose to trigger the events for this plugin. If Disabled, no events are triggered for this plugin.c

OnSlaveIdle.py

.. code-block:: python

    ###############################################################
    # Imports
    ###############################################################
    import math
    from System import *

    from Deadline.Events import *
    from Deadline.Scripting import *


    ##################################################################################################
    # This is the function called by Deadline to get an instance of the Draft event listener.
    ##################################################################################################
    def GetDeadlineEventListener():
        return OverrideMachineLimitListener()


    def CleanupDeadlineEventListener(eventListener):
        eventListener.Cleanup()


    ###############################################################
    # The event listener class.
    ###############################################################
    class OverrideMachineLimitListener(DeadlineEventListener):
        def __init__(self):
            self.OnSlaveIdleCallback += self.OnSlaveIdle

        def Cleanup(self):
            del self.OnSlaveIdleCallback

        def OnSlaveIdle(self, string):
            jobs = RepositoryUtils.GetJobsInState(["Active", "Pending"])
            # slaveInfos = RepositoryUtils.GetSlaveInfos(True)
            # slaves = [x for x in slaveInfos if x.SlaveState in ["Idle", "Rendering"]]
            # self.LogInfo("%d" % len(slaves))
            # enableSlaves = [x for x in slaveInfos if x.SlaveIsActive in ["Enable"]]
            # self.LogInfo("%d" % len(enableSlaves))
            # for slaveInfo in slaveInfos:
            #     self.LogInfo(slaveInfo.SlaveStatus)
            # INFO: AWSInfo,CPUUsage,CPUs,CompareTo,CompletedTasks,ConfigName,CurrentJobGroup,CurrentJobId,CurrentJobName,CurrentJobPool,CurrentJobPriority,CurrentJobUser,CurrentPlugin,CurrentTaskIds,CurrentTaskNames,CurrentTaskProgresses,CurrentTaskRenderTimes,CurrentTaskStatus,DiskReads,DiskSpace,DiskSpaceString,DiskWrites,Equals,ExtraElements,FailedTasks,Finalize,FreeMemory,FreeMode,GetHashCode,GetType,GroupsString,HostName,ID,IPAddress,IsAWSPortalInstance,IsLicensePermanent,IsLicensedByUsage,IsRunningAsService,LastReadRepoTime,LastReadTime,LastWriteTime,LicenseDaysLeftToExpiry,LicenseLastErrorMessage,LicenseServer,LimitGroupStubs,ListeningPort,MACAddress,MachineArchitecture,MachineCPUUsage,MachineCPUs,MachineDiskSpace,MachineFreeMemory,MachineIPAddress,MachineMACAddress,MachineMemory,MachineOperatingSystem,MachineProcessorSpeed,MachineRealName,MachineUserName,MachineVideoCard,MemberwiseClone,Memory,NetworkReceived,NetworkSent,OSShortName,OnLastTaskComplete,Overloads,PoolsString,ProcessorArchitecture,ProcessorSpeed,ReferenceEquals,Region,RenderingTime,SLAVE_NAME,SlaveCompletedTasks,SlaveConfigName,SlaveCurrentJobGroup,SlaveCurrentJobId,SlaveCurrentJobName,SlaveCurrentJobPool,SlaveCurrentJobPriority,SlaveCurrentJobUserName,SlaveCurrentPlugin,SlaveCurrentTaskIds,SlaveCurrentTaskNames,SlaveCurrentTaskProgresses,SlaveCurrentTaskRenderTimes,SlaveCurrentTaskStatus,SlaveFailedTasks,SlaveFreeMode,SlaveIsActive,SlaveIsLicensePermanent,SlaveIsLicensedByUsage,SlaveLastLicenseErrorMessage,SlaveLastMessage,SlaveLicenseDaysLeftToExpiry,SlaveLicenseServer,SlaveLimitGroupStubs,SlaveMessage,SlaveName,SlaveOnLastTaskComplete,SlaveRegion,SlaveRenderingTime,SlaveRunningTime,SlaveSettingsGroups,SlaveSettingsPools,SlaveState,SlaveStatus,StateDateTime,SwapUsage,ToString,UpTimeSeconds,UpdateDateTime,UserName,Version,VideoCard,__call__,__class__,__cmp__,__delattr__,__delitem__,__doc__,__format__,__getattribute__,__getitem__,__hash__,__init__,__iter__,__module__,__new__,__overloads__,__reduce__,__reduce_ex__,__repr__,__setattr__,__setitem__,__sizeof__,__str__,__subclasshook__,get_AWSInfo,get_CPUUsage,get_CPUs,get_CompletedTasks,get_ConfigName,get_CurrentJobGroup,get_CurrentJobId,get_CurrentJobName,get_CurrentJobPool,get_CurrentJobPriority,get_CurrentJobUser,get_CurrentPlugin,get_CurrentTaskIds,get_CurrentTaskNames,get_CurrentTaskProgresses,get_CurrentTaskRenderTimes,get_CurrentTaskStatus,get_DiskReads,get_DiskSpace,get_DiskSpaceString,get_DiskWrites,get_ExtraElements,get_FailedTasks,get_FreeMemory,get_FreeMode,get_GroupsString,get_HostName,get_ID,get_IPAddress,get_IsAWSPortalInstance,get_IsLicensePermanent,get_IsLicensedByUsage,get_IsRunningAsService,get_LastReadRepoTime,get_LastReadTime,get_LastWriteTime,get_LicenseDaysLeftToExpiry,get_LicenseLastErrorMessage,get_LicenseServer,get_LimitGroupStubs,get_ListeningPort,get_MACAddress,get_MachineArchitecture,get_MachineCPUUsage,get_MachineCPUs,get_MachineDiskSpace,get_MachineFreeMemory,get_MachineIPAddress,get_MachineMACAddress,get_MachineMemory,get_MachineOperatingSystem,get_MachineProcessorSpeed,get_MachineRealName,get_MachineUserName,get_MachineVideoCard,get_Memory,get_NetworkReceived,get_NetworkSent,get_OSShortName,get_OnLastTaskComplete,get_PoolsString,get_ProcessorArchitecture,get_ProcessorSpeed,get_Region,get_RenderingTime,get_SlaveCompletedTasks,get_SlaveConfigName,get_SlaveCurrentJobGroup,get_SlaveCurrentJobId,get_SlaveCurrentJobName,get_SlaveCurrentJobPool,get_SlaveCurrentJobPriority,get_SlaveCurrentJobUserName,get_SlaveCurrentPlugin,get_SlaveCurrentTaskIds,get_SlaveCurrentTaskNames,get_SlaveCurrentTaskProgresses,get_SlaveCurrentTaskRenderTimes,get_SlaveCurrentTaskStatus,get_SlaveFailedTasks,get_SlaveFreeMode,get_SlaveIsActive,get_SlaveIsLicensePermanent,get_SlaveIsLicensedByUsage,get_SlaveLastLicenseErrorMessage,get_SlaveLastMessage,get_SlaveLicenseDaysLeftToExpiry,get_SlaveLicenseServer,get_SlaveLimitGroupStubs,get_SlaveMessage,get_SlaveName,get_SlaveOnLastTaskComplete,get_SlaveRegion,get_SlaveRenderingTime,get_SlaveRunningTime,get_SlaveSettingsGroups,get_SlaveSettingsPools,get_SlaveState,get_SlaveStatus,get_StateDateTime,get_SwapUsage,get_UpTimeSeconds,get_UpdateDateTime,get_UserName,get_Version,get_VideoCard,set_AWSInfo,set_CPUUsage,set_CPUs,set_CompletedTasks,set_ConfigName,set_CurrentJobGroup,set_CurrentJobId,set_CurrentJobName,set_CurrentJobPool,set_CurrentJobPriority,set_CurrentJobUser,set_CurrentPlugin,set_CurrentTaskIds,set_CurrentTaskNames,set_CurrentTaskProgresses,set_CurrentTaskRenderTimes,set_CurrentTaskStatus,set_DiskReads,set_DiskSpace,set_DiskSpaceString,set_DiskWrites,set_ExtraElements,set_FailedTasks,set_FreeMemory,set_FreeMode,set_GroupsString,set_HostName,set_ID,set_IPAddress,set_IsAWSPortalInstance,set_IsLicensePermanent,set_IsLicensedByUsage,set_IsRunningAsService,set_LastReadRepoTime,set_LastReadTime,set_LastWriteTime,set_LicenseDaysLeftToExpiry,set_LicenseLastErrorMessage,set_LicenseServer,set_LimitGroupStubs,set_ListeningPort,set_MACAddress,set_Memory,set_NetworkReceived,set_NetworkSent,set_OSShortName,set_OnLastTaskComplete,set_PoolsString,set_ProcessorArchitecture,set_ProcessorSpeed,set_Region,set_RenderingTime,set_SlaveMessage,set_SlaveName,set_SlaveSettingsGroups,set_SlaveSettingsPools,set_SlaveStatus,set_StateDateTime,set_SwapUsage,set_UpTimeSeconds,set_UpdateDateTime,set_UserName,set_Version,set_VideoCard
            # self.LogInfo(",".join(dir(slaveInfos[0])))
            # INFO: Clone,Comment,ConcurrentTasksLimit,CpuAffinity,Description,EnableIdleCpuThreshold,EnableIdleProcessCheck,EnableIdleRamMBThreshold,EnableIdleRamPercentThreshold,EnableIdleUserCheck,Enabled,Equals,EventOptInArray,EventOptIns,EventOptInsStr,ExtraElements,ExtraInfo0,ExtraInfo1,ExtraInfo2,ExtraInfo3,ExtraInfo4,ExtraInfo5,ExtraInfo6,ExtraInfo7,ExtraInfo8,ExtraInfo9,ExtraInfoDictionary,Finalize,FinishTaskWhenStoppingIfNotIdle,GetHashCode,GetSlaveDataPath,GetSlaveExtraInfoKeyValue,GetSlaveExtraInfoKeyValueWithDefault,GetSlaveExtraInfoKeys,GetSlaveExtreInfoKeys,GetSlavePluginPath,GetType,GpuAffinity,GroupMappingID,Groups,HostMachineIPAddressOverride,ID,IdleCpuThreshold,IdleMinutes,IdleProcessNames,IdleRamMBThreshold,IdleRamPercentThreshold,IdleUserNames,IsCloudSlave,LastReadRepoTime,LastReadTime,LastWriteTime,ListeningPort,MacAddressOverride,MemberwiseClone,NormalizedRenderTimeMultiplier,NormalizedTimeoutMultiplier,OnlyStopSlaveIfStartedByIdleDetection,Overloads,OverrideCpuAffinity,OverrideGpuAffinity,OverrideListeningPort,OverrideSlaveScheduling,Pools,ReferenceEquals,Region,SLAVENAME,SchedulingMode,SetSlaveGroups,SetSlaveIdleProcessNames,SetSlaveIdleUserNames,SetSlavePools,SetSlaveUserJobsModeNames,SlaveComment,SlaveConcurrentTasksLimit,SlaveCpuAffinity,SlaveDescription,SlaveEnableIdleCpuThreshold,SlaveEnableIdleProcessCheck,SlaveEnableIdleRamMBThreshold,SlaveEnableIdleRamPercentThreshold,SlaveEnableIdleUserCheck,SlaveEnabled,SlaveExtraInfo0,SlaveExtraInfo1,SlaveExtraInfo2,SlaveExtraInfo3,SlaveExtraInfo4,SlaveExtraInfo5,SlaveExtraInfo6,SlaveExtraInfo7,SlaveExtraInfo8,SlaveExtraInfo9,SlaveExtraInfoDictionary,SlaveFinishTaskWhenStoppingIfNotIdle,SlaveGpuAffinity,SlaveGroups,SlaveHostMachineIPAddressOverride,SlaveIdleCpuThreshold,SlaveIdleMinutes,SlaveIdleProcessNames,SlaveIdleRamMBThreshold,SlaveIdleRamPercentThreshold,SlaveIdleUserNames,SlaveListeningPort,SlaveMacAddressOverride,SlaveName,SlaveNormalizedRenderTimeMultiplier,SlaveNormalizedTimeoutMultiplier,SlaveOnlyStopSlaveIfStartedByIdleDetection,SlaveOverrideCpuAffinity,SlaveOverrideGpuAffinity,SlaveOverrideListeningPort,SlaveOverrideSlaveScheduling,SlavePools,SlaveSchedulingMode,SlaveStartSlaveIfIdle,SlaveStopSlaveIfNotIdle,SlaveUserJobsModeNames,StartSlaveIfIdle,StopSlaveIfNotIdle,ToString,UseTmpDataPath,UserJobsModeNames,__call__,__class__,__cmp__,__delattr__,__delitem__,__doc__,__format__,__getattribute__,__getitem__,__hash__,__init__,__iter__,__module__,__new__,__overloads__,__reduce__,__reduce_ex__,__repr__,__setattr__,__setitem__,__sizeof__,__str__,__subclasshook__,get_Comment,get_ConcurrentTasksLimit,get_CpuAffinity,get_Description,get_EnableIdleCpuThreshold,get_EnableIdleProcessCheck,get_EnableIdleRamMBThreshold,get_EnableIdleRamPercentThreshold,get_EnableIdleUserCheck,get_Enabled,get_EventOptInArray,get_EventOptIns,get_EventOptInsStr,get_ExtraElements,get_ExtraInfo0,get_ExtraInfo1,get_ExtraInfo2,get_ExtraInfo3,get_ExtraInfo4,get_ExtraInfo5,get_ExtraInfo6,get_ExtraInfo7,get_ExtraInfo8,get_ExtraInfo9,get_ExtraInfoDictionary,get_FinishTaskWhenStoppingIfNotIdle,get_GpuAffinity,get_GroupMappingID,get_Groups,get_HostMachineIPAddressOverride,get_ID,get_IdleCpuThreshold,get_IdleMinutes,get_IdleProcessNames,get_IdleRamMBThreshold,get_IdleRamPercentThreshold,get_IdleUserNames,get_IsCloudSlave,get_LastReadRepoTime,get_LastReadTime,get_LastWriteTime,get_ListeningPort,get_MacAddressOverride,get_NormalizedRenderTimeMultiplier,get_NormalizedTimeoutMultiplier,get_OnlyStopSlaveIfStartedByIdleDetection,get_OverrideCpuAffinity,get_OverrideGpuAffinity,get_OverrideListeningPort,get_OverrideSlaveScheduling,get_Pools,get_Region,get_SchedulingMode,get_SlaveComment,get_SlaveConcurrentTasksLimit,get_SlaveCpuAffinity,get_SlaveDescription,get_SlaveEnableIdleCpuThreshold,get_SlaveEnableIdleProcessCheck,get_SlaveEnableIdleRamMBThreshold,get_SlaveEnableIdleRamPercentThreshold,get_SlaveEnableIdleUserCheck,get_SlaveEnabled,get_SlaveExtraInfo0,get_SlaveExtraInfo1,get_SlaveExtraInfo2,get_SlaveExtraInfo3,get_SlaveExtraInfo4,get_SlaveExtraInfo5,get_SlaveExtraInfo6,get_SlaveExtraInfo7,get_SlaveExtraInfo8,get_SlaveExtraInfo9,get_SlaveExtraInfoDictionary,get_SlaveFinishTaskWhenStoppingIfNotIdle,get_SlaveGpuAffinity,get_SlaveGroups,get_SlaveHostMachineIPAddressOverride,get_SlaveIdleCpuThreshold,get_SlaveIdleMinutes,get_SlaveIdleProcessNames,get_SlaveIdleRamMBThreshold,get_SlaveIdleRamPercentThreshold,get_SlaveIdleUserNames,get_SlaveListeningPort,get_SlaveMacAddressOverride,get_SlaveName,get_SlaveNormalizedRenderTimeMultiplier,get_SlaveNormalizedTimeoutMultiplier,get_SlaveOnlyStopSlaveIfStartedByIdleDetection,get_SlaveOverrideCpuAffinity,get_SlaveOverrideGpuAffinity,get_SlaveOverrideListeningPort,get_SlaveOverrideSlaveScheduling,get_SlavePools,get_SlaveSchedulingMode,get_SlaveStartSlaveIfIdle,get_SlaveStopSlaveIfNotIdle,get_SlaveUserJobsModeNames,get_StartSlaveIfIdle,get_StopSlaveIfNotIdle,get_UseTmpDataPath,get_UserJobsModeNames,set_Comment,set_ConcurrentTasksLimit,set_CpuAffinity,set_Description,set_EnableIdleCpuThreshold,set_EnableIdleProcessCheck,set_EnableIdleRamMBThreshold,set_EnableIdleRamPercentThreshold,set_EnableIdleUserCheck,set_Enabled,set_EventOptInArray,set_EventOptIns,set_EventOptInsStr,set_ExtraElements,set_ExtraInfo0,set_ExtraInfo1,set_ExtraInfo2,set_ExtraInfo3,set_ExtraInfo4,set_ExtraInfo5,set_ExtraInfo6,set_ExtraInfo7,set_ExtraInfo8,set_ExtraInfo9,set_ExtraInfoDictionary,set_FinishTaskWhenStoppingIfNotIdle,set_GpuAffinity,set_GroupMappingID,set_Groups,set_HostMachineIPAddressOverride,set_ID,set_IdleCpuThreshold,set_IdleMinutes,set_IdleProcessNames,set_IdleRamMBThreshold,set_IdleRamPercentThreshold,set_IdleUserNames,set_IsCloudSlave,set_LastReadRepoTime,set_LastReadTime,set_LastWriteTime,set_ListeningPort,set_MacAddressOverride,set_NormalizedRenderTimeMultiplier,set_NormalizedTimeoutMultiplier,set_OnlyStopSlaveIfStartedByIdleDetection,set_OverrideCpuAffinity,set_OverrideGpuAffinity,set_OverrideListeningPort,set_OverrideSlaveScheduling,set_Pools,set_Region,set_SchedulingMode,set_SlaveComment,set_SlaveConcurrentTasksLimit,set_SlaveCpuAffinity,set_SlaveDescription,set_SlaveEnableIdleCpuThreshold,set_SlaveEnableIdleProcessCheck,set_SlaveEnableIdleRamMBThreshold,set_SlaveEnableIdleRamPercentThreshold,set_SlaveEnableIdleUserCheck,set_SlaveEnabled,set_SlaveExtraInfo0,set_SlaveExtraInfo1,set_SlaveExtraInfo2,set_SlaveExtraInfo3,set_SlaveExtraInfo4,set_SlaveExtraInfo5,set_SlaveExtraInfo6,set_SlaveExtraInfo7,set_SlaveExtraInfo8,set_SlaveExtraInfo9,set_SlaveExtraInfoDictionary,set_SlaveFinishTaskWhenStoppingIfNotIdle,set_SlaveGpuAffinity,set_SlaveHostMachineIPAddressOverride,set_SlaveIdleCpuThreshold,set_SlaveIdleMinutes,set_SlaveIdleRamMBThreshold,set_SlaveIdleRamPercentThreshold,set_SlaveListeningPort,set_SlaveMacAddressOverride,set_SlaveName,set_SlaveNormalizedRenderTimeMultiplier,set_SlaveNormalizedTimeoutMultiplier,set_SlaveOnlyStopSlaveIfStartedByIdleDetection,set_SlaveOverrideCpuAffinity,set_SlaveOverrideGpuAffinity,set_SlaveOverrideListeningPort,set_SlaveOverrideSlaveScheduling,set_SlaveSchedulingMode,set_SlaveStartSlaveIfIdle,set_SlaveStopSlaveIfNotIdle,set_StartSlaveIfIdle,set_StopSlaveIfNotIdle,set_UseTmpDataPath,set_UserJobsModeNames
            slaveSettings = RepositoryUtils.GetSlaveSettingsList(True)
            # self.LogInfo(",".join(dir(slaveSettings[0])))
            slaves = [x for x in slaveSettings if x.SlaveEnabled]
            # self.LogInfo("%d" % len(slaves))
            # self.LogInfo(",".join(dir(jobs[0])))
            # for job in jobs:
            #     self.LogInfo(job.Name)
            #     self.LogInfo("%d" % job.JobTaskCount)
            # INFO: AWSPortalAssets,AuxiliarySubmissionFileNames,BadSlaves,BatchName,ChunkSize,Comment,CompletedChunks,CompletedDateTime,CompletedDateTimeString,CompletedFrames,ConcurrentTasks,CustomEventPluginDirectory,CustomPluginDirectory,DeleteJobEnvironmentKey,DeleteJobExtraInfoKey,Department,DisabledScheduleTime,EmailNotification,EnableAutoTimeout,EnableFrameTimeouts,EnableTimeoutsForScriptTasks,EnvironmentDictionary,Equals,ErrorReports,EventOptIns,ExtraElements,ExtraInfo0,ExtraInfo1,ExtraInfo2,ExtraInfo3,ExtraInfo4,ExtraInfo5,ExtraInfo6,ExtraInfo7,ExtraInfo8,ExtraInfo9,ExtraInfoDictionary,ExtraInfoKeyValues,FailedChunks,FailureDetectionJobErrors,FailureDetectionTaskErrors,Finalize,FirstFrame,FrameDependencyOffsetEnd,FrameDependencyOffsetStart,Frames,FramesList,FridayStartTime,FridayStopTime,GetEstimatedRemainingTime,GetFullOutputFileNamesForTask,GetFullOutputTileFileNamesForTask,GetHashCode,GetJobEnvironmentKeyValue,GetJobEnvironmentKeys,GetJobExtraInfoKeyValue,GetJobExtraInfoKeyValueWithDefault,GetJobExtraInfoKeys,GetJobInfoKeyValue,GetJobInfoKeys,GetJobPluginInfoKeyValue,GetJobPluginInfoKeys,GetOutputFileNamesForTask,GetOutputTileFileNamesForTask,GetType,GetUniqueHash,GetUniqueJobName,Group,HasDependencies,ID,IgnoreBadJobDetection,InitialCompletedTaskIds,InitialUncompletedTaskIds,InitializePluginTimeout,InitializePluginTimeoutSeconds,InterruptibleFlag,InterruptiblePercentage,IsBeingPurged,IsCorrupted,IsFrameDependent,IsSubmitted,JobAuxiliarySubmissionFileNames,JobBatchName,JobCleanupDays,JobComment,JobCompletedDateTime,JobCompletedTasks,JobConcurrentTasks,JobCustomEventPluginDirectory,JobCustomPluginDirectory,JobDepartment,JobDependencies,JobDependencyIDs,JobDependencyPercentage,JobDependencyPercentageValue,JobEmailNotification,JobEnableAutoTimeout,JobEnableFrameTimeouts,JobEnableTimeoutsForScriptTasks,JobExtraInfo0,JobExtraInfo1,JobExtraInfo2,JobExtraInfo3,JobExtraInfo4,JobExtraInfo5,JobExtraInfo6,JobExtraInfo7,JobExtraInfo8,JobExtraInfo9,JobFailedTasks,JobFailureDetectionJobErrors,JobFailureDetectionTaskErrors,JobForceReloadPlugin,JobFrameDependencyOffsetEnd,JobFrameDependencyOffsetStart,JobFrames,JobFramesList,JobFramesPerTask,JobFridayStartTime,JobFridayStopTime,JobGroup,JobId,JobIgnoreBadSlaveDetection,JobInfoFromJob,JobInitializePluginTimeoutSeconds,JobInterruptible,JobInterruptiblePercentage,JobIsFrameDependent,JobLimitGroups,JobLimitTasksToNumberOfCpus,JobListedSlaves,JobMachineLimit,JobMachineLimitProgress,JobMaintenanceJob,JobMaintenanceJobEndFrame,JobMaintenanceJobStartFrame,JobMinRenderTimeSeconds,JobMondayStartTime,JobMondayStopTime,JobName,JobNotificationEmails,JobNotificationNote,JobNotificationTargets,JobOnJobComplete,JobOnTaskTimeout,JobOutputDirectories,JobOutputFileNames,JobOutputTileFileNames,JobOverrideAutoJobCleanup,JobOverrideJobCleanup,JobOverrideJobCleanupDays,JobOverrideJobCleanupType,JobOverrideJobFailureDetection,JobOverrideNotificationMethod,JobOverrideTaskExtraInfoNames,JobOverrideTaskFailureDetection,JobPendingTasks,JobPlugin,JobPool,JobPopupNotification,JobPostJobScript,JobPostTaskScript,JobPreJobScript,JobPreTaskScript,JobPriority,JobProtected,JobQueuedTasks,JobRenderingTasks,JobRequiredAssets,JobResumeOnCompleteDependencies,JobResumeOnDeletedDependencies,JobResumeOnFailedDependencies,JobSaturdayStartTime,JobSaturdayStopTime,JobScheduledDays,JobScheduledStartDateTime,JobScheduledStopDateTime,JobScheduledType,JobScriptDependencies,JobSecondaryPool,JobSendJobErrorWarning,JobSequentialJob,JobStartJobTimeoutSeconds,JobStartedDateTime,JobStatus,JobSubmitDateTime,JobSubmitMachine,JobSundayStartTime,JobSundayStopTime,JobSuppressEvents,JobSuspendedTasks,JobSynchronizeAllAuxiliaryFiles,JobTaskCount,JobTaskExtraInfoName0,JobTaskExtraInfoName1,JobTaskExtraInfoName2,JobTaskExtraInfoName3,JobTaskExtraInfoName4,JobTaskExtraInfoName5,JobTaskExtraInfoName6,JobTaskExtraInfoName7,JobTaskExtraInfoName8,JobTaskExtraInfoName9,JobTaskTimeoutSeconds,JobThursdayStartTime,JobThursdayStopTime,JobTileJob,JobTileJobFrame,JobTileJobTileCount,JobTileJobTilesInX,JobTileJobTilesInY,JobTuesdayStartTime,JobTuesdayStopTime,JobUseJobEnvironmentOnly,JobUserName,JobWednesdayStartTime,JobWednesdayStopTime,JobWhitelistFlag,LastFrame,LastWriteTime,LimitGroups,LimitTasksToNumberOfCpus,ListedSlaves,LogReportFileNames,LogReportLastWriteTime,MachineLimit,MachineLimitProgress,MaintenanceJob,MaintenanceJobEndFrame,MaintenanceJobStartFrame,MemberwiseClone,MinRenderTime,MinRenderTimeSeconds,MondayStartTime,MondayStopTime,Name,NotificationEmails,NotificationNote,NotificationTargets,OnJobComplete,OnTaskTimeout,OutputDirectories,OutputFileNames,OutputTileFileNames,Overloads,OverrideAutoJobCleanup,OverrideJobCleanup,OverrideJobCleanupType,OverrideJobFailureDetection,OverrideNotificationMethod,OverrideTaskExtraInfoNames,OverrideTaskFailureDetection,PathMappingRules,PendingChunks,PluginDataFileName,PluginDataFileSize,PluginInfoDictionary,PluginName,Pool,PopupNotification,PostJobScript,PostTaskScript,PreJobScript,PreTaskScript,Priority,Properties,Protected,QueuedChunks,ReferenceEquals,RegionName,ReloadRenderer,RemTimeThreshold,RenderingChunks,RequiredAssets,ResumeOnCompleteDependencies,ResumeOnDeletedDependencies,ResumeOnFailedDependencies,SanitizeJob,SaturdayStartTime,SaturdayStopTime,ScheduledDays,ScheduledStartDateTime,ScheduledStopDateTime,ScheduledType,ScriptDependencies,SecondaryPool,SendJobErrorWarning,SequentialJobFlag,SetDefaults,SetJobDependencyIDs,SetJobEnvironmentKeyValue,SetJobExtraInfoKeyValue,SetJobLimitGroups,SetJobNotificationEmails,SetJobNotificationTargets,SetJobPluginInfoKeyValue,SetJobRequiredAssets,SetScriptDependencies,SingleTaskProgress,StartJobTimeout,StartJobTimeoutSeconds,StartedDateTime,StartedDateTimeString,Status,SubmitDateTime,SubmitDateTimeString,SubmitMachineName,SubmitUserName,SundayStartTime,SundayStopTime,SuppressEvents,SuspendedChunks,SynchronizeAllAuxiliaryFiles,TaskCount,TaskExtraInfoName0,TaskExtraInfoName1,TaskExtraInfoName2,TaskExtraInfoName3,TaskExtraInfoName4,TaskExtraInfoName5,TaskExtraInfoName6,TaskExtraInfoName7,TaskExtraInfoName8,TaskExtraInfoName9,TaskTimeout,TaskTimeoutSeconds,ThursdayStartTime,ThursdayStopTime,TileJob,TileJobFrame,TileJobTileCount,TileJobTilesInX,TileJobTilesInY,ToInfoString,ToString,TotalRenderTime,TotalRenderTimeTicks,TuesdayStartTime,TuesdayStopTime,UseJobEnvironmentOnly,UserName,WednesdayStartTime,WednesdayStopTime,WhitelistFlag,__call__,__class__,__cmp__,__delattr__,__delitem__,__doc__,__format__,__getattribute__,__getitem__,__hash__,__init__,__iter__,__module__,__new__,__overloads__,__reduce__,__reduce_ex__,__repr__,__setattr__,__setitem__,__sizeof__,__str__,__subclasshook__,get_AWSPortalAssets,get_AuxiliarySubmissionFileNames,get_BadSlaves,get_BatchName,get_ChunkSize,get_Comment,get_CompletedChunks,get_CompletedDateTime,get_CompletedDateTimeString,get_CompletedFrames,get_ConcurrentTasks,get_CustomEventPluginDirectory,get_CustomPluginDirectory,get_Department,get_EmailNotification,get_EnableAutoTimeout,get_EnableFrameTimeouts,get_EnableTimeoutsForScriptTasks,get_EnvironmentDictionary,get_ErrorReports,get_EventOptIns,get_ExtraElements,get_ExtraInfo0,get_ExtraInfo1,get_ExtraInfo2,get_ExtraInfo3,get_ExtraInfo4,get_ExtraInfo5,get_ExtraInfo6,get_ExtraInfo7,get_ExtraInfo8,get_ExtraInfo9,get_ExtraInfoDictionary,get_ExtraInfoKeyValues,get_FailedChunks,get_FailureDetectionJobErrors,get_FailureDetectionTaskErrors,get_FirstFrame,get_FrameDependencyOffsetEnd,get_FrameDependencyOffsetStart,get_Frames,get_FramesList,get_FridayStartTime,get_FridayStopTime,get_Group,get_ID,get_IgnoreBadJobDetection,get_InitialCompletedTaskIds,get_InitialUncompletedTaskIds,get_InitializePluginTimeout,get_InitializePluginTimeoutSeconds,get_InterruptibleFlag,get_InterruptiblePercentage,get_IsBeingPurged,get_IsFrameDependent,get_IsSubmitted,get_JobAuxiliarySubmissionFileNames,get_JobBatchName,get_JobCleanupDays,get_JobComment,get_JobCompletedDateTime,get_JobCompletedTasks,get_JobConcurrentTasks,get_JobCustomEventPluginDirectory,get_JobCustomPluginDirectory,get_JobDepartment,get_JobDependencies,get_JobDependencyIDs,get_JobDependencyPercentage,get_JobDependencyPercentageValue,get_JobEmailNotification,get_JobEnableAutoTimeout,get_JobEnableFrameTimeouts,get_JobEnableTimeoutsForScriptTasks,get_JobExtraInfo0,get_JobExtraInfo1,get_JobExtraInfo2,get_JobExtraInfo3,get_JobExtraInfo4,get_JobExtraInfo5,get_JobExtraInfo6,get_JobExtraInfo7,get_JobExtraInfo8,get_JobExtraInfo9,get_JobFailedTasks,get_JobFailureDetectionJobErrors,get_JobFailureDetectionTaskErrors,get_JobForceReloadPlugin,get_JobFrameDependencyOffsetEnd,get_JobFrameDependencyOffsetStart,get_JobFrames,get_JobFramesList,get_JobFramesPerTask,get_JobFridayStartTime,get_JobFridayStopTime,get_JobGroup,get_JobId,get_JobIgnoreBadSlaveDetection,get_JobInitializePluginTimeoutSeconds,get_JobInterruptible,get_JobInterruptiblePercentage,get_JobIsFrameDependent,get_JobLimitGroups,get_JobLimitTasksToNumberOfCpus,get_JobListedSlaves,get_JobMachineLimit,get_JobMachineLimitProgress,get_JobMaintenanceJob,get_JobMaintenanceJobEndFrame,get_JobMaintenanceJobStartFrame,get_JobMinRenderTimeSeconds,get_JobMondayStartTime,get_JobMondayStopTime,get_JobName,get_JobNotificationEmails,get_JobNotificationNote,get_JobNotificationTargets,get_JobOnJobComplete,get_JobOnTaskTimeout,get_JobOutputDirectories,get_JobOutputFileNames,get_JobOutputTileFileNames,get_JobOverrideAutoJobCleanup,get_JobOverrideJobCleanup,get_JobOverrideJobCleanupDays,get_JobOverrideJobCleanupType,get_JobOverrideJobFailureDetection,get_JobOverrideNotificationMethod,get_JobOverrideTaskExtraInfoNames,get_JobOverrideTaskFailureDetection,get_JobPendingTasks,get_JobPlugin,get_JobPool,get_JobPopupNotification,get_JobPostJobScript,get_JobPostTaskScript,get_JobPreJobScript,get_JobPreTaskScript,get_JobPriority,get_JobProtected,get_JobQueuedTasks,get_JobRenderingTasks,get_JobRequiredAssets,get_JobResumeOnCompleteDependencies,get_JobResumeOnDeletedDependencies,get_JobResumeOnFailedDependencies,get_JobSaturdayStartTime,get_JobSaturdayStopTime,get_JobScheduledDays,get_JobScheduledStartDateTime,get_JobScheduledStopDateTime,get_JobScheduledType,get_JobScriptDependencies,get_JobSecondaryPool,get_JobSendJobErrorWarning,get_JobSequentialJob,get_JobStartJobTimeoutSeconds,get_JobStartedDateTime,get_JobStatus,get_JobSubmitDateTime,get_JobSubmitMachine,get_JobSundayStartTime,get_JobSundayStopTime,get_JobSuppressEvents,get_JobSuspendedTasks,get_JobSynchronizeAllAuxiliaryFiles,get_JobTaskCount,get_JobTaskExtraInfoName0,get_JobTaskExtraInfoName1,get_JobTaskExtraInfoName2,get_JobTaskExtraInfoName3,get_JobTaskExtraInfoName4,get_JobTaskExtraInfoName5,get_JobTaskExtraInfoName6,get_JobTaskExtraInfoName7,get_JobTaskExtraInfoName8,get_JobTaskExtraInfoName9,get_JobTaskTimeoutSeconds,get_JobThursdayStartTime,get_JobThursdayStopTime,get_JobTileJob,get_JobTileJobFrame,get_JobTileJobTileCount,get_JobTileJobTilesInX,get_JobTileJobTilesInY,get_JobTuesdayStartTime,get_JobTuesdayStopTime,get_JobUseJobEnvironmentOnly,get_JobUserName,get_JobWednesdayStartTime,get_JobWednesdayStopTime,get_JobWhitelistFlag,get_LastFrame,get_LastWriteTime,get_LimitGroups,get_LimitTasksToNumberOfCpus,get_ListedSlaves,get_LogReportFileNames,get_LogReportLastWriteTime,get_MachineLimit,get_MachineLimitProgress,get_MaintenanceJob,get_MaintenanceJobEndFrame,get_MaintenanceJobStartFrame,get_MinRenderTime,get_MinRenderTimeSeconds,get_MondayStartTime,get_MondayStopTime,get_Name,get_NotificationEmails,get_NotificationNote,get_NotificationTargets,get_OnJobComplete,get_OnTaskTimeout,get_OutputDirectories,get_OutputFileNames,get_OutputTileFileNames,get_OverrideAutoJobCleanup,get_OverrideJobCleanup,get_OverrideJobCleanupType,get_OverrideJobFailureDetection,get_OverrideNotificationMethod,get_OverrideTaskExtraInfoNames,get_OverrideTaskFailureDetection,get_PathMappingRules,get_PendingChunks,get_PluginDataFileName,get_PluginDataFileSize,get_PluginInfoDictionary,get_PluginName,get_Pool,get_PopupNotification,get_PostJobScript,get_PostTaskScript,get_PreJobScript,get_PreTaskScript,get_Priority,get_Properties,get_Protected,get_QueuedChunks,get_RegionName,get_ReloadRenderer,get_RemTimeThreshold,get_RenderingChunks,get_RequiredAssets,get_ResumeOnCompleteDependencies,get_ResumeOnDeletedDependencies,get_ResumeOnFailedDependencies,get_SaturdayStartTime,get_SaturdayStopTime,get_ScheduledDays,get_ScheduledStartDateTime,get_ScheduledStopDateTime,get_ScheduledType,get_ScriptDependencies,get_SecondaryPool,get_SendJobErrorWarning,get_SequentialJobFlag,get_SingleTaskProgress,get_StartJobTimeout,get_StartJobTimeoutSeconds,get_StartedDateTime,get_StartedDateTimeString,get_Status,get_SubmitDateTime,get_SubmitDateTimeString,get_SubmitMachineName,get_SubmitUserName,get_SundayStartTime,get_SundayStopTime,get_SuppressEvents,get_SuspendedChunks,get_SynchronizeAllAuxiliaryFiles,get_TaskCount,get_TaskExtraInfoName0,get_TaskExtraInfoName1,get_TaskExtraInfoName2,get_TaskExtraInfoName3,get_TaskExtraInfoName4,get_TaskExtraInfoName5,get_TaskExtraInfoName6,get_TaskExtraInfoName7,get_TaskExtraInfoName8,get_TaskExtraInfoName9,get_TaskTimeout,get_TaskTimeoutSeconds,get_ThursdayStartTime,get_ThursdayStopTime,get_TileJob,get_TileJobFrame,get_TileJobTileCount,get_TileJobTilesInX,get_TileJobTilesInY,get_TotalRenderTime,get_TotalRenderTimeTicks,get_TuesdayStartTime,get_TuesdayStopTime,get_UseJobEnvironmentOnly,get_UserName,get_WednesdayStartTime,get_WednesdayStopTime,get_WhitelistFlag,s_dateTimeParseString,s_jobIdRegex,set_AWSPortalAssets,set_AuxiliarySubmissionFileNames,set_BadSlaves,set_BatchName,set_ChunkSize,set_Comment,set_CompletedChunks,set_CompletedDateTime,set_CompletedDateTimeString,set_CompletedFrames,set_ConcurrentTasks,set_CustomEventPluginDirectory,set_CustomPluginDirectory,set_Department,set_EmailNotification,set_EnableAutoTimeout,set_EnableFrameTimeouts,set_EnableTimeoutsForScriptTasks,set_ErrorReports,set_EventOptIns,set_ExtraElements,set_ExtraInfo0,set_ExtraInfo1,set_ExtraInfo2,set_ExtraInfo3,set_ExtraInfo4,set_ExtraInfo5,set_ExtraInfo6,set_ExtraInfo7,set_ExtraInfo8,set_ExtraInfo9,set_ExtraInfoDictionary,set_ExtraInfoKeyValues,set_FailedChunks,set_FailureDetectionJobErrors,set_FailureDetectionTaskErrors,set_FrameDependencyOffsetEnd,set_FrameDependencyOffsetStart,set_FramesList,set_FridayStartTime,set_FridayStopTime,set_Group,set_ID,set_IgnoreBadJobDetection,set_InitialCompletedTaskIds,set_InitialUncompletedTaskIds,set_InitializePluginTimeout,set_InitializePluginTimeoutSeconds,set_InterruptibleFlag,set_InterruptiblePercentage,set_IsBeingPurged,set_IsFrameDependent,set_IsSubmitted,set_JobBatchName,set_JobCleanupDays,set_JobComment,set_JobConcurrentTasks,set_JobCustomEventPluginDirectory,set_JobCustomPluginDirectory,set_JobDepartment,set_JobDependencies,set_JobDependencyPercentage,set_JobDependencyPercentageValue,set_JobEmailNotification,set_JobEnableAutoTimeout,set_JobEnableFrameTimeouts,set_JobEnableTimeoutsForScriptTasks,set_JobExtraInfo0,set_JobExtraInfo1,set_JobExtraInfo2,set_JobExtraInfo3,set_JobExtraInfo4,set_JobExtraInfo5,set_JobExtraInfo6,set_JobExtraInfo7,set_JobExtraInfo8,set_JobExtraInfo9,set_JobFailureDetectionJobErrors,set_JobFailureDetectionTaskErrors,set_JobForceReloadPlugin,set_JobFrameDependencyOffsetEnd,set_JobFrameDependencyOffsetStart,set_JobFridayStartTime,set_JobFridayStopTime,set_JobGroup,set_JobIgnoreBadSlaveDetection,set_JobInitializePluginTimeoutSeconds,set_JobInterruptible,set_JobInterruptiblePercentage,set_JobIsFrameDependent,set_JobLimitTasksToNumberOfCpus,set_JobMinRenderTimeSeconds,set_JobMondayStartTime,set_JobMondayStopTime,set_JobName,set_JobNotificationNote,set_JobOnJobComplete,set_JobOnTaskTimeout,set_JobOverrideAutoJobCleanup,set_JobOverrideJobCleanup,set_JobOverrideJobCleanupDays,set_JobOverrideJobCleanupType,set_JobOverrideJobFailureDetection,set_JobOverrideNotificationMethod,set_JobOverrideTaskExtraInfoNames,set_JobOverrideTaskFailureDetection,set_JobPool,set_JobPopupNotification,set_JobPostTaskScript,set_JobPreTaskScript,set_JobPriority,set_JobProtected,set_JobResumeOnCompleteDependencies,set_JobResumeOnDeletedDependencies,set_JobResumeOnFailedDependencies,set_JobSaturdayStartTime,set_JobSaturdayStopTime,set_JobScheduledDays,set_JobScheduledStartDateTime,set_JobScheduledStopDateTime,set_JobScheduledType,set_JobSecondaryPool,set_JobSendJobErrorWarning,set_JobSequentialJob,set_JobStartJobTimeoutSeconds,set_JobSundayStartTime,set_JobSundayStopTime,set_JobSuppressEvents,set_JobSynchronizeAllAuxiliaryFiles,set_JobTaskExtraInfoName0,set_JobTaskExtraInfoName1,set_JobTaskExtraInfoName2,set_JobTaskExtraInfoName3,set_JobTaskExtraInfoName4,set_JobTaskExtraInfoName5,set_JobTaskExtraInfoName6,set_JobTaskExtraInfoName7,set_JobTaskExtraInfoName8,set_JobTaskExtraInfoName9,set_JobTaskTimeoutSeconds,set_JobThursdayStartTime,set_JobThursdayStopTime,set_JobTuesdayStartTime,set_JobTuesdayStopTime,set_JobUseJobEnvironmentOnly,set_JobUserName,set_JobWednesdayStartTime,set_JobWednesdayStopTime,set_LastWriteTime,set_LimitGroups,set_LimitTasksToNumberOfCpus,set_ListedSlaves,set_LogReportFileNames,set_LogReportLastWriteTime,set_MachineLimit,set_MachineLimitProgress,set_MaintenanceJob,set_MaintenanceJobEndFrame,set_MaintenanceJobStartFrame,set_MinRenderTime,set_MinRenderTimeSeconds,set_MondayStartTime,set_MondayStopTime,set_Name,set_NotificationEmails,set_NotificationNote,set_NotificationTargets,set_OnJobComplete,set_OnTaskTimeout,set_OutputDirectories,set_OutputFileNames,set_OutputTileFileNames,set_OverrideAutoJobCleanup,set_OverrideJobCleanup,set_OverrideJobCleanupType,set_OverrideJobFailureDetection,set_OverrideNotificationMethod,set_OverrideTaskExtraInfoNames,set_OverrideTaskFailureDetection,set_PathMappingRules,set_PendingChunks,set_PluginDataFileName,set_PluginDataFileSize,set_PluginName,set_Pool,set_PopupNotification,set_PostJobScript,set_PostTaskScript,set_PreJobScript,set_PreTaskScript,set_Priority,set_Properties,set_Protected,set_QueuedChunks,set_RegionName,set_ReloadRenderer,set_RemTimeThreshold,set_RenderingChunks,set_RequiredAssets,set_ResumeOnCompleteDependencies,set_ResumeOnDeletedDependencies,set_ResumeOnFailedDependencies,set_SaturdayStartTime,set_SaturdayStopTime,set_ScheduledDays,set_ScheduledStartDateTime,set_ScheduledStopDateTime,set_ScheduledType,set_ScriptDependencies,set_SecondaryPool,set_SendJobErrorWarning,set_SequentialJobFlag,set_SingleTaskProgress,set_StartJobTimeout,set_StartJobTimeoutSeconds,set_StartedDateTime,set_StartedDateTimeString,set_Status,set_SubmitDateTime,set_SubmitDateTimeString,set_SubmitMachineName,set_SundayStartTime,set_SundayStopTime,set_SuppressEvents,set_SuspendedChunks,set_SynchronizeAllAuxiliaryFiles,set_TaskCount,set_TaskExtraInfoName0,set_TaskExtraInfoName1,set_TaskExtraInfoName2,set_TaskExtraInfoName3,set_TaskExtraInfoName4,set_TaskExtraInfoName5,set_TaskExtraInfoName6,set_TaskExtraInfoName7,set_TaskExtraInfoName8,set_TaskExtraInfoName9,set_TaskTimeout,set_TaskTimeoutSeconds,set_ThursdayStartTime,set_ThursdayStopTime,set_TileJob,set_TileJobFrame,set_TileJobTileCount,set_TileJobTilesInX,set_TileJobTilesInY,set_TotalRenderTime,set_TotalRenderTimeTicks,set_TuesdayStartTime,set_TuesdayStopTime,set_UseJobEnvironmentOnly,set_UserName,set_WednesdayStartTime,set_WednesdayStopTime,set_WhitelistFlag

            if jobs and slaves:
                userNum = len(set(job.UserName for job in jobs if job.JobTaskCount != 2))
                self.LogInfo("User Num: %d" % userNum)
                self.LogInfo("Machine Num: %d" % len(slaves))

                if not userNum:
                    return

                num = int(math.ceil(float(len(slaves)) / float(userNum)))

                if userNum == 1:

                    for job in jobs:

                        if job.MachineLimit != 0:
                            self.LogInfo(job.Name)
                            RepositoryUtils.SetMachineLimitMaximum(job.ID, 0)

                else:

                    for job in jobs:

                        if job.MachineLimit != num:
                            self.LogInfo(job.Name)
                            RepositoryUtils.SetMachineLimitMaximum(job.ID, num)
