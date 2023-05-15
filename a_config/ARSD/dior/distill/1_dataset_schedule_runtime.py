dataset_type = 'DiorDataset'
data_root = '/home/airstudio/data/'
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(type='Resize', img_scale=(800, 800), keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(800, 800),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=32),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
data = dict(
    samples_per_gpu=8,
    workers_per_gpu=2,
    train=dict(
        type=dataset_type,
        ann_file=data_root + 'DIOR/ImageSets/Main/trainval.txt',
        img_prefix=data_root + 'DIOR/',
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        ann_file=data_root + 'DIOR/ImageSets/Main/test.txt',
        img_prefix=data_root + 'DIOR/',
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        ann_file=data_root + 'DIOR/ImageSets/Main/test.txt',
        img_prefix=data_root + 'DIOR/',
        pipeline=test_pipeline))
evaluation = dict(interval=1, metric='mAP')

# optimizer
optimizer = dict(type='SGD', lr=0.005, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)
# optimizer_config = dict(grad_clip=dict(max_norm=35, norm_type=2))
# learning policy
lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=500,
    warmup_ratio=0.001,
    step=[20, 28])
total_epochs = 30

checkpoint_config = dict(interval=1)
# yapf:disable
log_config = dict(
    interval=50,
    hooks=[
        dict(type='TextLoggerHook'),
        # dict(type='TensorboardLoggerHook')
    ])
# yapf:enable
dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = None
resume_from = None
workflow = [('train', 1)]

# resume_from = '/workspace/a_yyr_code/yyr/work_dirs_dior/dis_bk+cls+reg_m_g_c_mask4//latest.pth'
# todo fpn
# work_dir = './work_dirs_dior/dis_atss101_18_f0.5_dior_mask4'
# todo fpn + cls
# work_dir = './work_dirs_dior/dis_atss101_18_f0.5_dior_cls_bk_mask3'
# todo fpn + reg
# work_dir = './work_dirs_dior/dis_atss101_18_f0.5_dior_reg_bk_mask4'
# todo fpn + reg +cls
# work_dir = './work_dirs_dior/dis_bk+cls+reg_m_g_c_mask4'
# work_dir = './work_dirs_diors/dis_reg_s_0.1c_giou_cls_bk_mask4'
# work_dir = './work_dirs_diors/dis_reg_s_0.1_giou_cls_bk_mask4'
# work_dir = 'tuui'

work_dir = './work_dirs/d_bk_m4'