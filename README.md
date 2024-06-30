# AI-Agentic-Design-Patterns-with-AutoGen
Use the AutoGen framework to build multi-agent systems with diverse roles and capabilities for implementing complex AI applications.  Implement agentic design patterns: Reflection, Tool use, Planning, and Multi-agent collaboration using AutoGen.  Learn directly from the creators of AutoGen, Chi Wang and Qingyun Wu.
## AutoGen 文档： https://microsoft.github.io/autogen/docs/Getting-Started
### L1 两个agent 对话(郭德纲跟于谦讲相声)，并总结对话，查看使用量
### L2 多个agent 连续对话完成一项任务（一个模拟客户agent(需要用户输入),两个信息收集agent,最后一个agent根据前面收集的数据进行扩展生成）
### L3  两个agent之间对话，其中一个agent 嵌套一套任务 chat流，完成任务流chat 后，在总结返回给第一个agent
### L4  在嵌套模块的基础上调用工具（tool） 进行下棋（可以两个机器人agent,也可以有人为输入 human_input_mode="ALWAYS"）
### L5  两个coding agnet ，第一个会执行代码，第二个会利用人提供建议生成代码，然后两个agent合作完成代码编写任务（可以调用自定义的 function）
### L6  定义群聊， manager 管理群聊，群聊中admin接受任务和指令， planner做计划分解任务给其他agent, 其他agent 完成子任务 ，这样就不用把任务流人工写死了

